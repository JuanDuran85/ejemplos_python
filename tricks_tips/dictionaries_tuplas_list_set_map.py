"""[summary]

Tips and tricks for using dictionaries, tuples, lists, and sets in Python.

All the examples are in the same file, but they are separated with a mark

All examples are from the internet with somes variations, so they are not 100% correct. Thanks to the authors.

"""

"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using lists - Can be: ordered, mutable, duplicates'''
print("\n Using lists \n")
n_values_in_list = ["", 0, None, -3, 5, [], 1, {}, 7.5]
n_values_in_list_two = range(0,10,2)
print(f"{n_values_in_list = }")
print(f"{n_values_in_list_two = }")

# You can use the filter method to filter a list of values, in this case, the values ​​None or empty. Be careful with the zero value.
print(f"{list(filter(None, n_values_in_list)) = }")


"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using tuples - Can be: ordered, inmutable, duplicates'''
print("\n Using tuples \n")
players = ("Messi", "Ronaldo", "Neymar", "Suarez", "Pele", "Maradona", "Pirlo", "Ribery", "Bale")
print(f"{players = }")

# If you need yo get the first index of a given value inside a tuple, you can use the index method.
print(f"{players.index('Pele') = }")



"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using dictionaries - Can be: ordered, mutable, no duplicate keys'''
print("\n Using dictionaries \n")

user = {
    "name": "Arlene",
    "lastname": "Sipes",
    "age": 40
}
print(f"Completed {user = }")

# if you want to get all the values ​​and keys in a dictionary, you can use the items method in a loop.
for key,value in user.items():
    print(f"--> {key}: {value}") 

# you can use the popitem method to delete the last item in the dictionary, and save the key and value in a variable.
key, value = user.popitem()
print(f"{key = } and {value = } deleted")
print(f"New dictionary {user = }") 

# The get() method on dicts has a default value if the key is not found. 
def greeting(key_user):
    return "Hi %s!" % user.get(key_user, "there")
print(f"{greeting('name') = }")
print(f"{greeting('names') = }")

# If you want to merge two dictionaries, you can use the unpacking operator.
x = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
}

y = {
    'a': 10,
    'f': 3,
    'c': 20,
    'o': -1,
    'p': 5,
}

# In the first example, the unpacking operator will be used on both dictionaries, overwriting duplicates from left to right.
z = {**x, **y}
print("{**x, **y} = ", z)
w = dict(x, **y)
print("dict(x, **y) = ", w)

# If you need to sort a Python dict by value, you can use the sorted method.
dict_sort = {'a': 4, 'b': 2, 'c': 1, 'd': 3}
print(f"{sorted(dict_sort.items(), key=lambda x: x[1]) = }")
print(dict_sort.items())

"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using set - Can be: unordered, mutable, no duplicates'''
print("\n Using set \n")
people_a = { 'Shanna', 'Cara', 'Bessie' , 'Antonio' , 'Jordy' }
people_b = { 'Cathryn', 'Bessie', 'Federico', 'Jordy', 'Camille', 'Cara' }
print(f"{people_a = }")
print(f"{people_b = }")

# you can use isdisjoint() to check intersection of two sets is empty.
print(f"{people_a.isdisjoint(people_b) = }")

# use method .intersection to get a new set containing only the elements that are in both sets
print(f"{people_a.intersection(people_b) = }")

# use method .union to get a new set containing all the elements from both sets
print(f"{people_a.union(people_b) = }")

"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using map '''




"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using zip '''
print("\n Using zip \n")
list_numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"{list_numbers = }")

# use zip function to make N-tuples from N arguments, so it can be used with *args to transpose a list of lists.
print(f"{list(zip(*list_numbers)) = }")


"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Convination of lists, tuples, dictionaries, set, map, zip '''
print("\n Convination of lists, tuples, dictionaries, set, map \n")
numbers_a_bases = [1,2,3,4]
numbers_b_exponents = [2,3,2,3]
users = ['Shanna', 'Bessie', 'Cara', 'Antonio', 'Bessie', 'Cara', 'Antonio' , 'Jordy', 'Cara']
print(f"{numbers_a_bases = }")
print(f"{numbers_b_exponents = }")
print(f"{users = }")

# You can use the map and the list with two iterables to obtain a list with the result of numbers raised to the power n of another list.
print(f"{list(map(pow, numbers_a_bases, numbers_b_exponents)) = }")

# If you need remove duplicades from a list, you can use diccionaries with loops and preserve the order of the elements.
print(f"{list({user: user for user in users}) = }")

# If you need to remove duplicates from a list, you can use set and generate a new list, but you lose the order of the elements.
print(f"{list(set(users)) = }")

# If you need to remove duplicates from a list, you can use the fromkeys and list method to generate a new list, but you lose the order of the elements.
print(f"{list(dict.fromkeys(users)) = }")

"""----------------------------------------------------------------------------------------"""