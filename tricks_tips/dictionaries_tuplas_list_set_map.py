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

# use An assignment expression (sometimes also called a “named expression” or “walrus”) to assign a value to a variable.
numbers: list = [2,8,0,1,1,9,7,7]
descripction: dict = {
    "length": (num_length := len(numbers)),
    "sum": (num_sum := sum(numbers)),
    "mean": (num_sum / num_length),
}

print(f"{descripction = }")

# use Walrus to evaluated the value of an input
while (command := input("Ingresa quit para salir: ")) != "quit": print(f"Ingresaste {command}")

# ------------------------------------------------------------------------------------------

users: list = ["Mike", "John", "Smith"]
print(f"{users = }")
# you can reverse the order of a list with the reverse() method and other methods.
# example 1: use reversed - it returns iterator, you need to convert it to list
print(f"{list(reversed(users)) = }")
# example 2: use slicing from begining to end using negative step
print(f"{users[::-1] = }")
# example 3: use .reverse()
users.reverse()
print(f"{users = }")

# Finding Highest Frequency Element: We can find the element, which occurs the maximum time, by passing the key as the count of elements, in the example, the number of times they appear.
list_numbers: list = [5,3,2,6,3,21,5,3,1,5,3,2,7,8,8,5,3,9,9,1]
print("Most frequent item: ", max(set(list_numbers), key=list_numbers.count))

#------------------------------------------------------------------------------------
# Deleting Multiple Elements from a List
list_number: list = [1,2,3,4,5]
print(f"{list_number = }")
del list_number[1:4]
print(f"{ list_number = }")

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

# You can mix dictionaries using the ** kwargs operator.
dictionary_one: dict = {'1':'one','2':'two','3':'three'}
result_dict: dict = dict(**dictionary_one, x_value=56)
print(f"{result_dict = }")
result_dict_two: dict = dict(**dictionary_one, x_value="Nuevo valor", **{'4':'four'})
print(f"{result_dict_two = }")

print("There is more than one method where you can merge two dictionaries.")
dict_one: dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

dict_two: dict = {
    'f': 3,
    'a': 10,
    'd': 4,
}

print(f"{dict_one = }")
print(f"{dict_two = }")

# The first method uses dictionary unpacking where the two dictionaries unpack together into result. 
print("first method")
result_merge: dict = {**dict_one, **dict_two}
print(f"{result_merge = }")

# The second method, we first copy the first dictionary into the result and then update it with the content of the second dictionary. 
print("second method")
result_merge_two: dict = dict_one.copy()
result_merge_two.update(dict_two)
print(f"{result_merge_two = }")

# The third method is a straightforward implementation using dictionary comprehension, similar to what we saw in list comprehension above.
print("second method")
result_merge_three: dict = {key: value for d in (dict_one,dict_two) for key, value in d.items()}
print(f"{result_merge_three = }")


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

# use zip to set the list to a dictionary with keys and values
keys: list = ['nombre','ciudad','edad']
values: list = ['Juan','Santiago','40']
dict_result: dict = {}
for key, dict_result[key] in zip(keys, values): ...
print(f"{dict_result = }")

# use zip to get the key and value of a list of tuples
args_list: list = [(2,3),(2,4),(2,4)]
print(f"{args_list = }")
base, exponents = zip(*args_list)
print(f"{base = }")
print(f"{exponents = }")

# use zip to set two lists to a dictionary
users: list = ["Juan", "Pedro", "Maria"]
user_visit: list = [354,456,23]
for user, visits in zip(users, user_visit):
    print(f"{user = } and {visits = }")

"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Convination of lists, tuples, dictionaries, set, map, zip '''
print("\n Convination of lists, tuples, dictionaries, set, map \n")

# you can use the map function with list and pow to get the power of each element in the list.
args_list_pow: list = [(2,3),(2,4),(2,4)]

print(f"{list(map(pow, base,exponents)) = }")

#---------------------------------------------------------------------------------------------
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

# you can merge two lists into a dictionary with different methods
countries: list = ['Colombia','Chile','Spain','Brazil','Gabon','Indonesia']
codes: list = ['CO','CL','ES','BR','GA','ID']

# First: Using indexing
dictionarie_indexing: dict = {}
for i in range(len(codes)):
    dictionarie_indexing[codes[i]] = countries[i]
print(f"{dictionarie_indexing = }")

# Second: Using zip
dictionary_zip: dict = {}
for code,country in zip(codes,countries):
    dictionary_zip[code] = country
print(f"{dictionary_zip = }") 

# Thirds: Replacing loop with dict comprehension
dictionary_comprehension: dict = {code: country for code, country in zip(codes, countries)}
print(f"{dictionary_comprehension = }")

# Fourth: Replace dict comprehension with dict call
dictionary_final: dict = dict(zip(codes, countries))
print(f"{dictionary_final = }")

#-------------------------------------------
# You can use the zip function to make N-tuples from N arguments, so it can be used with *args to transpose a list of lists.
first: list = ['Mickey', 'Harry', 'Sherlock']
last: list = ['Mouse', 'Potter', 'Holmes']
names = list(zip(first, last))
print(f"{names = }")
first_names, last_names = zip(*names)
print(f"{first_names = }")
print(f"{last_names = }")

# You can use the unpack function to unpack a list or tuple or range into a large list
my_tuple: tuple = (45,567,132,9)
my_list: list = ['texto uno', 'otro texto', 'mas palabras en string']
my_range: range = range(5)
final_combo: list = [*my_tuple, *my_list, *my_range]
print(f"{final_combo = }")

# if you want to remove duplicate items in a list you can use different options
duplicate_items_list: list = [34,56,2,34,2,45,56,2,34]
print(f"{duplicate_items_list = }")
cleaned_items_list: list = list(set(duplicate_items_list))
print(f"{cleaned_items_list = }")
cleaned_items_list_two: list = list(dict.fromkeys(duplicate_items_list))
print(f"{cleaned_items_list_two = }")

# use enumerate to extrac all the characters from a string in a dictionary
string_to_print: str = "python"
dict_result: dict = {}
for i, dict_result[i] in enumerate(string_to_print):
    i = 1
print(f"{dict_result = }")

#------------------------------------------------------------------
# Sorting a list of dictionaries, we can do it using two different, yet similar approaches. We can simply use the in-built sorted() or sort() function which works on lists using a lambda function inside it which sorts the dictionaries based on their ‘id’ key

person: list = [
    {
        'name': 'Anne',
        'age': '34',
        'id': '21657'
    },
    {
        'name': 'Lucinda',
        'age': '67',
        'id': '18058'
    },
    {
        'name': 'Fabiola',
        'age': '12',
        'id': '31216'
    },
]
print(f"{person = }")

# first approach: a new list of sorted dictionaries is returned. A custom key function can be supplied to customize the sort order, and the reverse flag can be set to request the result in descending order.
person_sort: list = sorted(person, key= lambda item: item.get('id'))
print(f"{person_sort = }")

# second approach: the return type is None as the changes are in place
person.sort(key= lambda item: item.get('id'))
print(f"{person = }")

# -----------------------------------------------------------------------------------------
# Sum of Even Numbers In a List using a List Comprehension and SUM() function
list_number: list = [3,5,6,2,8,9,1,0,6]
print(f"{list_number = }")
sum_even_number: int = sum([number for number in list_number if number % 2 == 0])
print(f"{sum_even_number = }")

"""----------------------------------------------------------------------------------------"""
