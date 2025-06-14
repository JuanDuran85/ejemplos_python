# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103
# working with while loop


"""[summary]

Tips and tricks for using string, conditions, loop, others.

All the examples are in the same file, but they are separated with a mark

All examples are from the internet with some variations, so they are not 100% correct. Thanks to the authors.

Using string methods

"""

from typing import Literal


LINES = "---------------------------------------------------------------------\r"


print("\n Using count \n")
LETTERS_ANY = "aaabbbcccdddeeffffff"
print(f"{LETTERS_ANY=}")

# if you need to count any letter in a string you can use count method
print(f"{LETTERS_ANY.count('a')=}")
print(f"{LETTERS_ANY.count('f')=}")
print(f"{LETTERS_ANY.count('d')=}")

# if you want to print a list in one row, use 'join' and list comprehension
row_list: list = ["1", "elio", "developer", "python"]
print(f"{','.join(str(x) for x in row_list)=}")
# if you want to print a list in one row, use print with * and sep arguments
print(*row_list, sep=',')

# If you need to print a string n times
print("This is a separator", "-"*50)

print(LINES)
print("Different ways to test multiple flags at once in Python")

print("\n Different ways to test multiple flags at once\n")

x, y, z = 0, 0, 0

if x == 1 or y == 1 or z == 1:
    print("True")
else:
    print("False")

if 1 in (x, y, z):
    print("True")
else:
    print("False")

# These only test for truthiness, not for equality.
if x or y or z:
    print("True")
else:
    print("False")

if any((x, y, z)):
    print("True")
else:
    print("False")

# use the all function if you need to test true on all elements of a tuple
if all((x, y, z)):
    print("All True")

# Check if these strings only contain alphabetic characters
print("\n Check if these strings only contain alphabetic characters\n")
print(all(char.isalnum() for char in "textovario"))
print(all(char.isalnum() for char in "spaces are not allowed"))

# if you want to return a binary string "Unicode code point for all characters strings"


def make_bit_seq(character_in: str) -> str:
    """
    Converts a string of ASCII characters into a binary string representation.

    Each character in the input string is converted to its Unicode code point,
    and then formatted as an 8-bit binary number. The function raises a ValueError
    if the input string contains non-ASCII characters.

    Args:
        character_in (str): A string of ASCII characters to be converted.

    Returns:
        str: A binary string representation of the input characters.

    Raises:
        ValueError: If the input string contains non-ASCII characters.
    """

    if not character_in.isascii():
        raise ValueError("Only ascii characters are allowed")
    return "".join(f"{ord(i):08b}" for i in character_in)


print(make_bit_seq("bits"))
print(make_bit_seq("TRICKS"))
print(make_bit_seq("lower caps"))
print(make_bit_seq("$25.43"))

# if you need to get the position of a character in a string you can use for loop to get it in three different options
i: int = 0
s: str = 'abc'

# option 1
for c in s:
    print(f"{i}: {c}")
    i += 1

# option 2
for i, c in enumerate(s):
    print(f"{i}: {c}")

i = 0
# option 3
for key, value in enumerate(s, start=1):
    print(f"{key}: {value}")

# You can use zfill to add zeros to the left of a string
print(f"{'293'.zfill(10)=}")

# use rjust to add a character to the right of a string. Return a right-justified string of length width.
print(f"{'Juan'.rjust(10, '*')=}")

# Use sep in the print function to separate the string
print("123", "345", "654", sep="-")

# -------------------------------------------------------------------------------
# Finding Substring in List of Strings

records: list = [
    "Vani Gupta, University of Hyderabad",
    "Elon Musk, Tesla",
    "Bill Gates, Microsoft",
    "Steve Jobs, Apple"
]

# If we need to find substrings inside a list of strings (can also be applied on larger strings rather than just lists),
# we can use the find() method which returns -1 if the value is not present in the string,
# or returns the first occurrence.

name: str = "Vani"
for record in records:
    if record.find(name) >= 0:
        print(f"{name} found in {record}")


# In the second method, we can directly use the 'in' operator to see if the desired substring is present in the string.
name: str = "Musk"
for record in records:
    if name in record:
        print(f"{name} found in {record}")

# --------------------------------------------------------------------------------
# FizzBuzz One-Liner in Python: The FizzBuzz challenge is a classic challenge that's used as an interview screening device for computer programmers. You can solve the FizzBuzz challenge in just one line of code

[print("Fizz"*(i % 3 == 0)+"Buzz"*(i % 5 == 0) or i) for i in range(1, 20)]

# --------------------------------------------------------------------------------------
# Conditional Expressions: The conditional expression’s value is set to expr2 if the outcome is true. The conditional expression’s value is set to expr3 if the outcome is false.

# Instead or this... for example:


def is_even(num: int) -> None:
    """
    Checks if a number is even or odd.

    Args:
        num (int): The number to be checked.

    Returns:
        None
    """
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# use this way


def is_even_one(num: int) -> None:
    print(f"{num} is even" if num % 2 == 0 else f"{num} is odd")

# or use this way


def is_even_two(num: int) -> None:
    print(f"{num} is even") if num % 2 == 0 else print(f"{num} is odd")


is_even(5)
is_even_two(5)
is_even_two(5)

# ----------------------------------------------------------------------
# Comparison Operator: you can use one line comparator withy logical operator. For example:
num: int = 100
if 25 < num < 150:
    print(f"{num} is between 25 and 150")

# is you want to initialize a variable with a value in one line, you can use the following way:
initial_num: int = 100
final_num: Literal[21, 42] = 21 if initial_num < 2 else 42
print(f"{final_num}")

# elif in one line
print("no") if final_num > 42 else print("yes") if final_num == 42 else print("maybe")

# If without else in one line
print("hello") if final_num > 42 else print("no")

# While Loop with if else
count_number: int = 0
while count_number < 10:
    count_number += 1
    print(count_number) if count_number != 5 else print("-Five-")


# Nested For Loops in one line
iter1: list = [1, 2, 3, 4]
iter2: list = ['a', 'b', 'c']
[print(x, y) for x in iter1 for y in iter2]

# -------------------------------------------------------------------------
# Swapping Two Variables
a: int = 4
b: int = -23
a, b = b, a
print(f"{a} {b}")

# Multiple Variable Assignments
a, b, c = 3, 5, 'Python'
print(f"{a} {b} {c}")

# you cab use * to assign variables from a list
a, b, *c = [1, 2, 3, 4, 5, 6, 7]
print(f"{a} {b} {c}")


# ------------------------------------------------------------------------------
text_any: str = '7792'
result_text: list = text_any.split('-')
print(result_text)
print(f"{result_text[2]}" if len(result_text) > 1 else None)

# ------------------------------------------------------------------------------
# using all to Return True if bool(x) is True for all values x in the iterable. If the iterable is empty, return True.


def contains_only_vowels(word: str) -> bool:
    """
    Checks if a given word contains only vowel characters.

    The function converts the input word to lowercase and verifies that
    each character in the word is a vowel ('a', 'e', 'i', 'o', 'u').

    Args:
        word (str): The word to be checked.

    Returns:
        bool: True if the word contains only vowels, False otherwise.
    """

    word = word.lower()
    vowels = 'aeiou'
    return all(c in vowels for c in word)


print(contains_only_vowels('Python'))
print(contains_only_vowels('Juan'))
print(contains_only_vowels('AEI'))

# -----------------------------------------------------------------------------------
# if you want to split a string and join it back
my_string: str = "This is a tex string"
print(f"String original text without modification: {my_string}")
my_string_list: list = my_string.split()
my_string_new_list: list = [text.title() for text in my_string_list]
final_my_string: str = " ".join(my_string_new_list)
print(f"Modified text from string: {final_my_string}")

# -----------------------------------------------------------------------------------
# two different ways to print a list in one line
# option 1
row: list = ["1", "juan", "developer", "python"]
print(','.join(str(x) for x in row))

# option 2
print(*row, sep=',')

# -----------------------------------------------------------------------------------
# Thousand Separator

n = 100000000000
print(f"{n:,}")

# -----------------------------------------------------------------------------------
#

print(LINES)
print(LINES)

print("Using the Walrus Operator for Smarter Code")
# The Problem
# You need to use a variable inside a conditional only once, but you haven’t quite defined it yet!
# The walrus operator (:=) allows us to compute and check a value in a single step.

calories: list[int] = [464, 678, 323, 221, 876, 174, 265, 985]

if (total_calories := sum(calories)) > 2000:
    avg_calories = total_calories / len(calories)
    print(f"Average calories per day: {avg_calories}")

print(LINES)
print(LINES)


# -----------------------------------------------------------------------------------
print("Using Immutable Defaults to Avoid Silent Bugs")
# -----------------------------------------------------------------------------------
# use None as the default argument, and initialize a new list inside the function.


def record_loss(loss: str, loss_history: list[str] | None = None):
    """Record a loss in a list of losses.

    Args:
        loss: The loss to record.
        loss_history: The list of losses to append to. If None, a new list is created.

    Returns:
        The list of losses with the new loss appended.
    """
    if loss_history is None:
        loss_history = []
    loss_history.append(loss)
    return loss_history


print(record_loss("Loss 1"))
print(record_loss("Loss 2", ["loss 345"]))

print(LINES)
print(LINES)
