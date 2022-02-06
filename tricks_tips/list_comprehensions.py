"""[summary]

Tips and tricks for using list comprehensions in Python.

All the examples are in the same file, but they are separated with a mark

All examples are from the internet with somes variations, so they are not 100% correct. Thanks to the authors.

"""

import random


"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using lists comprehension '''
print("\n Using lists comprehension \n")

n_numbers = 20
cuantity_products = {
    "banana": 5,
    "apple": 10,
    "mango": 3,
    "peach": 2,
    "wathermelon": 1
}
fruits = ["peach", "banana", "apple"]
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"{n_numbers = }")
print(f"{cuantity_products = }")
print(f"{fruits = }")
print(f"{numbers_list = }")

# you can use list comprehension and random library to create a list with the result of n random numbers in another list.
list_of_numbers = [random.randint(1,100) for _ in range(n_numbers)]
print(f"{list_of_numbers = }")

# You can use list comprehension to get the value of the key in the dictionary from a list of keys.
print(f"cuantity products: {[cuantity_products[fruit] for fruit in fruits] }")

# use list comprehension to get the first n squares of the numbers in the list.
print(f"{[n**2 for n in numbers_list] = }")


"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""