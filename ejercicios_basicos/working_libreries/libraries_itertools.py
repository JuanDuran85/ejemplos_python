"""_sumary_:

    Usando la libreria itertools
    Using itertools library
    Using zip_longest

"""

from itertools import accumulate, filterfalse, zip_longest

"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using lists - Can be: ordered, mutable, duplicates'''
print("\n Using lists with itertools \n")

n_values_in_list_two = range(0,10,2)
print(f"{n_values_in_list_two = }")

# With accumulate from itertools librery, you can sum the values ​​in a list
print(f"{list(accumulate(n_values_in_list_two)) = }")


# The filterfalse function creates a iterator that filters elements from iterable returning only those for which the predicate is False 
list_any: list = [None, True, 1, 0, False, '', [], {}, [1,2], {'a':1}, 'string...']
list_filter: list = list(filterfalse(bool, list_any))
print(f"{list_filter = }")


# If you want to zip uneven list in Python, you can either accept that one list will be truncated ot you can use zip_longest from itertools library

x: list = [1, 2, 3, 4, 5]
y: list = ['a', 'b', 'c']

result_x_y: list = list(zip_longest(x, y))
print(f"{result_x_y = }")