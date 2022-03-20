"""[summary]

    Using operator library

"""

import operator
from functools import reduce

# If you need to sort a Python dict by value, you can use the sorted method and the operator library.
dict_sort = {'a': 4, 'b': 2, 'c': 1, 'd': 3}
print(f"{sorted(dict_sort.items(), key=operator.itemgetter(1)) = }")

# Use the mul function to multiply all the values in a list
numbers: list = [1,2,3,4,5]
print(f"{reduce(operator.mul, numbers) = }")
