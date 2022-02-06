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

# You can use the filter method to filter a list of values, in this case, the values ​​None or empty. Be careful with the zero value.
print(f"{list(filter(None, n_values_in_list)) = }")


"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using tuples - Can be: ordered, inmutable, duplicates'''

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

"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using set - Can be: unordered, mutable, no duplicates'''
print("\n Using set \n")
people_a = { 'Shanna', 'Cara', 'Bessie' , 'Antonio' , 'Jordy' }
people_b = { 'Cathryn', 'Bessie', 'Federico', 'Jordy', 'Camille', 'Cara' }
print(f"{people_a = }")
print(f"{people_b = }")

# use method .intersection to get a new set containing only the elements that are in both sets
print(f"{people_a.intersection(people_b) = }")

# use method .union to get a new set containing all the elements from both sets
print(f"{people_a.union(people_b) = }")

"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using map '''



"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Convination of lists, tuples, dictionaries, set, map '''
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