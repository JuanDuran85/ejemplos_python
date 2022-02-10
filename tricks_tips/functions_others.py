"""[summary]

Tips and tricks for functions.

All the examples are in the same file, but they are separated with a mark

All examples are from the internet with somes variations, so they are not 100% correct. Thanks to the authors.

"""
"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using functions '''
print("\n Using functions \n")

''' 
Functions are first-class citizens in Python. They can be passed as arguments to other functions, returned by other functions, and assigned to variables.
'''

def my_function(x,y):
    return x + y

functions = [my_function]
print(f"{functions[0](4,2) = } ")

''' Using functions unpacking'''
print("\n Using function argument unpacking \n")

def function_one(x,y,z):
    return x + y + z

tuple_values = (3,6,1)
dict_values = {
    'x': 3,
    'y': 6,
    'z': 1
}
print(f"{tuple_values = }")
print(f"{dict_values = }")
print(f"{function_one(*tuple_values) = } ")
print(f"{function_one(**dict_values) = } ")