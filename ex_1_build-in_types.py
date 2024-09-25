from enum import auto, IntFlag
from typing import Any

from pydantic import (
    BaseModel,  # basic validation system of pydantic
    EmailStr,  # this specific type has basic email validation inside
    Field,
    SecretStr,
    ValidationError,
)


class Role(IntFlag):
    Author = auto()
    Editor = auto()
    Developer = auto()
    Admin = Author | Editor | Developer


class User(BaseModel):
    name: str = Field(examples=["Arjan"])
    email: EmailStr = Field(
        examples=["example@arjancodes.com"],
        description="The email address of the user",  # this will use for FastAPI docs
        frozen=True,
    )
    password: SecretStr = Field(
        examples=["Password123"], description="The password of the user"
    )
    role: Role = Field(default=None, description="The role of the user")


def validate(data: dict[str, Any]) -> None:
    try:
        user = User.model_validate(data)
        print(user)
    except ValidationError as e:
        print("User is invalid")
        for error in e.errors():
            print(error)


def main() -> None:
    good_data = {
        "name": "Arjan",
        "email": "example@arjancodes.com",
        "password": "Password123",
    }
    bad_data1 = {"email": "<bad data>", "password": "<bad data>"}

    validate(good_data)
    validate(bad_data1)


if __name__ == "__main__":
    main()
