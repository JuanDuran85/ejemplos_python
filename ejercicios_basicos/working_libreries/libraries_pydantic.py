"""
Working with pydantic library

Data validation and settings management using Python type annotations.
pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.
Define how data should be in pure, canonical Python; validate it with pydantic.

"""

from pydantic import BaseModel
from datetime import datetime

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

class User(BaseModel):
    id: int = 0
    name: str = "No name"
    first_in: datetime | None = None
    languages: list[str] = []


example_data: dict = {
    "id": '1',
    "first_in": '2022-11-07 22:46',
    "languages": ["Python","Javascript","C++"]
}

user_one: User = User(**example_data)
print(user_one.id)
print(user_one.first_in)
print(user_one.dict())

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


