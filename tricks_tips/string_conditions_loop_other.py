"""[summary]

Tips and tricks for using string, conditions, loop, others.

All the examples are in the same file, but they are separated with a mark

All examples are from the internet with somes variations, so they are not 100% correct. Thanks to the authors.

"""

"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using string methods'''

print("\n Using count \n")
letters_any = "aaabbbcccdddeeffffff"
print(f"{letters_any = }")

# if you need to count any letter in a string you can use count method
print(f"{letters_any.count('a') = }")
print(f"{letters_any.count('f') = }")
print(f"{letters_any.count('d') = }")

# if you want to print a list in one row, use 'join' and list comprehension
row_list: list = ["1","elio","developer","python"]
print(f"{ ','.join(str(x) for x in row_list)  = }")
# if you want to print a list in one row, use print with * and sep arguments
print(*row_list, sep=',')



"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Diferent ways to test multiple flags at once in Python'''

print("\n Diferent ways to test multiple flags at once\n")

x, y, z = 0, 0, 0

if x==1 or y==1 or z==1:
    print("True")
else:
    print("False")
    
if 1 in (x,y,z):
    print("True")
else: 
    print("False")

# These only test for truthiness, not for equality.
if x or y or z:
    print("True")
else:
    print("False")
    
if any((x,y,z)):
    print("True")
else:
    print("False")
    
# use the all function if you need to test true on all elements of a tuple
if all((x,y,z)):
    print("All True")
    
# Check if these strings only contain alphabetic characters
print("\n Check if these strings only contain alphabetic characters\n")
print(all(char.isalnum() for char in "textovario"))
print(all(char.isalnum() for char in "texto vario con espacio"))

# if you want to return a binary string "Unicode code point for all characters strings"
def make_bitseq(character_in: str) -> str:
    if not character_in.isascii():
        raise ValueError("Only ascii characters are allowed")
    return "".join(f"{ord(i):08b}" for i in character_in)

print(make_bitseq("bits"))
print(make_bitseq("TRICKS"))
print(make_bitseq("lower caps"))
print(make_bitseq("$25.43"))

# if you need to get the position of a character in a string you can use for loop to get it in three different options
i: int = 0
s: str = 'abc'

# option 1
for c in s:
    print(f"{i}: {c}")
    i += 1
    
# option 2
for i,c in enumerate(s):
    print(f"{i}: {c}")

i = 0    
# option 3
for key,value in enumerate(s, start=1):
    print(f"{key}: {value}")
    
# You can use zfill to add zeros to the left of a string
print(f"{'293'.zfill(10) = }")

# use rjust to add a character to the right of a string. Return a right-justified string of length width.
print(f"{'Juan'.rjust(10,'*') = }")

# Use sep in the print function to separate the string
print("123","345","654", sep="-")

# -------------------------------------------------------------------------------
# Finding Substring in List of Strings

records: list = [
    "Vani Gupta, University of Hyderabad",
    "Elon Musk, Tesla",
    "Bill Gates, Microsoft",
    "Steve Jobs, Apple"
]

# If we need to find substrings inside a list of strings (can also be applied on larger strings rather than just lists), we can use the find() method which returns -1 if the value is not present in the string, or returns the first occurrence. 

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

[print("Fizz"*(i%3==0)+"Buzz"*(i%5==0) or i) for i in range(1,20)]

# --------------------------------------------------------------------------------------
# Conditional Expressions: The conditional expression’s value is set to expr2 if the outcome is true. The conditional expression’s value is set to expr3 if the outcome is false.

# Instead or this... for example:
def is_even(num: int) -> None:
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
# Comparison Operator: you can use one line comparation withy logical operator. For example:
num: int = 100
if 25 < num < 150:
    print(f"{num} is between 25 and 150")

