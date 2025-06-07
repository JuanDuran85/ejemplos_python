# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

"""
Working with pydantic library

Data validation and settings management using Python type annotations.
pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.
Define how data should be in pure, canonical Python; validate it with pydantic.

"""

from datetime import datetime

from pydantic import BaseModel, ValidationError

LINES = "---------------------------------------------------------------------\r"

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

print(LINES)
print(LINES)


class User(BaseModel):
    """
    Represents a user with an ID, name, optional first login datetime, and a list of programming languages.
    """
    id: int = 0
    name: str = "No name"
    first_in: datetime | None = None
    languages: list[str] = []


example_data: dict = {
    "id": '1',
    "first_in": '2022-11-07 22:46',
    "languages": ["Python", "Javascript", "C++"]
}

user_one: User = User(**example_data)
print(user_one.id)
print(user_one.first_in)
print(user_one.model_dump())

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

try:
    User(first_in='broken', languages=[1, 2, 'not number'])  # type: ignore
except ValidationError as e:
    print(e.json())

print(LINES)
print(LINES)
# If you need to validate data structures like tuples, dataclasses,
# or even custom objects with specific attribute types or sophisticated constraints,
# Pydantic provides a powerful and elegant solution.
# Instead of writing multiple assertions or type checks manually,
# you can simply define a BaseModel that handles validation automatically.


class UserFinal(BaseModel):
    """
    Represents a user with name, age, and address fields.
    Validates data types using Pydantic's BaseModel.
    """
    name: str
    age: int
    address: str


try:
    user = UserFinal(
        name="John",
        age="He dont have age",  # type: ignore
        address="Street 1"
    )
except ValidationError as e:
    print("Validation error: ", e)

print(LINES)
print(LINES)
