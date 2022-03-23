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
names_list = ['Jayce','Thelma','Blair','Arvilla','Wava','Cassandre','Antonia','Grace']
print(f"{n_numbers = }")
print(f"{cuantity_products = }")
print(f"{fruits = }")
print(f"{numbers_list = }")
print(f"{ names_list = }")

# you can use list comprehension and random library to create a list with the result of n random numbers in another list.
list_of_numbers = [random.randint(1,100) for _ in range(n_numbers)]
print(f"{list_of_numbers = }")

# You can use list comprehension to get the value of the key in the dictionary from a list of keys.
print(f"cuantity products: {[cuantity_products[fruit] for fruit in fruits] }")

# use list comprehension to get the first n squares of the numbers in the list.
print(f"{[n**2 for n in numbers_list] = }")

# use list comprehension to get the names with n charters in the list x.
print(f"{[name for name in names_list if len(name) == 5] = }")


# Use list comprehension with split to get the first word of each sentence in a list.
sentences: list = ["Primer texto de la cadena", "Segundo texto de la cadena", "Tercer texto de la cadena", "Cuarto texto de la cadena"]
first_words = [sentence.split()[0] for sentence in sentences]
print(f"{first_words = }")

# If you have a list of string, you can get the list of first letters
sentences_name: list = ["Juan","Jose","Maria","Petra","Josefina","Ignacia"]
result_list: list = [name[0] for name in sentences_name]
print(f"{result_list = }")

# Use list comprehension to get all the methods of a dictionary.
values_dict: dict = {'bob':'11', 'julian':'22','tim':'33','jose':'44'}
result_method: list = [attr for attr in dir(values_dict) if not attr.startswith('__')]
print(f"{result_method = }")
print(values_dict.keys())

# Use list comprehension to extract the keys of a dictionary when using a list.
prices: dict = {
    "milk": 1,
    "bread": 2,
    "coffee": 3,
    "butter": 4,
    "tea": 5,
    "banana": 6
}

products: list = ["milk","tea","butter"]

print(f"{ [prices[product] for product in products]  = }")

"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""

# In the following code, we can see that we are checking multiples of 6, and then multiples of 2 and 3 using the if-else conditions inside the list, which reduced the code to a great extent.

list_final: list = ['Multiplo de 6' if i%6 == 0 else 'Multiplo de 2' if i%2 == 0 else 'Multiplo de 3' if i % 3 == 0 else i for i in range(1,15)]
print(f"{list_final = }")