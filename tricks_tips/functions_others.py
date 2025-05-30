"""[summary]

Tips and tricks for functions.

All the examples are in the same file, but they are separated with a mark

All examples are from the internet with somes variations, so they are not 100% correct. Thanks to the authors.

You can use Docstrings to describe the function and help methods to show the documentation.

"""
"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using functions '''

print("\n Using functions \n")

''' 
Functions are first-class citizens in Python. They can be passed as arguments to other functions, returned by other functions, and assigned to variables.
'''


def my_function(x, y):
    return x + y


functions = [my_function]
print(f"{functions[0](4, 2)=} ")

''' Using functions unpacking'''
print("\n Using function argument unpacking \n")


def function_one(x, y, z):
    return x + y + z


tuple_values = (3, 6, 1)
dict_values = {
    'x': 3,
    'y': 6,
    'z': 1
}
print(f"{tuple_values=}")
print(f"{dict_values=}")
print(f"{function_one(*tuple_values)=} ")
print(f"{function_one(**dict_values)=} ")

'''
    In Python, you can define a function's arguments to be positional-only. In order to do that, you just use a '/' in the argument list. What comes before the '/' is positional-only
'''

print(f"\r\nArguments Positional-Only\r\n")


def example_function(a: int, b: int, /) -> int:
    return a+b


print(example_function(1, 4))
# print(example_function(1,b=4)), In this case, we catch an error, because the arguments in the function are only positional


'''
    Becouse Python has first-class functions they can be use to emulate switch/case statements
'''


def dispatch_if(operator: str, x: int, y: int):
    if operator == 'add':
        return x + y
    elif operator == 'sub':
        return x - y
    elif operator == 'mul':
        return x * y
    elif operator == 'div':
        return x / y
    else:
        return None


def dispatch_dict(operator: str, x: int, y: int):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


print(f"{dispatch_if('add', 1, 2)=} ")
print(f"{dispatch_dict('add', 1, 2)=} ")

# ----------------------------------------------------------------------------------------------
# Use * in functions to use positional arguments


def my_function_two(*, a, b) -> None:
    print(a, b)


my_function_two(a=1, b=2)
# my_function_two(1,2) # Error, because the function only needs positional arguments

# -----------------------------------------------------------------------------------------------
# Use * in functions parameters to use keyword arguments
# find the smallest number passed as argument in a function


def find_smallest_number(*values) -> int:

    # using min() function to find the smallest number
    lower_value: int = min(values)
    print(f"{lower_value=}")
    # -------------------------------------------------
    # using for loop to find the smallest number
    lower_value_two: int = values[0]
    for value in values:
        if (value < lower_value_two):
            lower_value_two = value
    return lower_value_two


print(find_smallest_number(1, -2, 3, 24, 5, 6, -7, 8, 9, -10))

# ------------------------------------------------------------------------------------------------
# Use ** in functions parameters to use keyword arguments


def print_parameters(**values) -> None:
    for key, value in values.items():
        print(f"{key} -> {value}")


print_parameters(a=1, b=2, c=3, d=4, e=5)
