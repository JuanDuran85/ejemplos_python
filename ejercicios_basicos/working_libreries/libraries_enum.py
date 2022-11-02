"""[summary]

Usage: Library enum

An enumeration:
    is a set of symbolic names (members) bound to unique values
    can be iterated over to return its members in definition order
    uses call syntax to return members by value
    uses index syntax to return members by name
    
Enumerations are created either by using class syntax, or by using function-call syntax

"""

from enum import Enum, auto

#--------------------------------------------------------------------------------
'''
auto: can be used in place of a value. If used, the Enum machinery will call an Enum’s _generate_next_value_() to get an appropriate value. For Enum and IntEnum that appropriate value will be the last value plus one; for Flag and IntFlag it will be the first power-of-two greater than the last value; for StrEnum it will be the lower-cased version of the member’s name.
 _generate_next_value_ can be overridden to customize the values used by auto.
'''
#--------------------------------------------------------------------------------
class Animal(Enum):
    CAT = auto()
    DOG = auto()
    BIRD = auto()

print(f"{ list(Animal) = }")
print(f"{ Animal.CAT = }")
print(f"{ Animal.DOG = }")
#--------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
# You can access to enums in a couple of different ways. For example, you can access by number or using attributes, or also have dictionary-like access: ex. Languages["Python"]
#--------------------------------------------------------------------------------
class Languages(Enum):
    PYTHON = 1
    JAVASCRIPT = 2
    CPLUSPLUS = 3

print(f"{Languages(2) = }")
print(f"{Languages(1) = }")

code_result = Languages.CPLUSPLUS
print(f"{code_result.name = }")
print(f"{code_result.value = }")

print(f"{Languages['PYTHON'] = }")

#--------------------------------------------------------------------------------