"""[summary]

Usage: Library enum

"""

from enum import Enum, auto

class Animal(Enum):
    CAT = auto()
    DOG = auto()
    BIRD = auto()

print(f"{ list(Animal) = }")
print(f"{ Animal.CAT = }")