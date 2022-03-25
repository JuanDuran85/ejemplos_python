"""_summary_

    Using pipe library.
    
    Pipe is a Python library that enables you to use pipes in Python. A pipe ( | ) passes the results of one method to another method. Pipe only provides a few methods.
    
    You can insert one method after another method using pipes. As a result, using
    pipes removes nested parentheses and makes the code more readable.

"""

from pipe import select, where, chain, traverse

arr: list = [1,2,3,4,5,]
print(f"{arr = }")

# Where — Filter Elements in an Iterable. Similar to SQL, Pipe’s where method can also be used to filter elements in an iterable.
nuevo_arr: list = list(arr | where(lambda x: x % 2 == 0) | select(lambda x: x * 2))

print(f"{nuevo_arr = }")

# Select — Apply a Function to an Iterable. The select method is similar to the map method. select applies a method to each element of an iterable.

nuevo_arreglo_dos: list = list(arr | select(lambda x: x * 2))
print(f"{nuevo_arreglo_dos = }")

# chain — Chain a Sequence of Iterables. It can be a pain to work with a nested iterable. Luckily, you can use chain to chain a sequence of iterables.

nested_list: list = [[1,2, [3]], [4,5]]
print(f"{nested_list = }")
nuevo_arreglo_tres: list = list(nested_list | chain )
print(f"{nuevo_arreglo_tres = }")

# traverse — Recursively Unfold Iterables. The traverse method can be used to recursively unfold iterables. Thus, you can use this method to turn a deeply nested list into a flat list.
nested_list_two: list = [[1,2,[3]],[4],5,6,[7]]
nuevo_arreglo_cuatro: list = list(nested_list_two | traverse)
print(f"{nuevo_arreglo_cuatro = }")

# traverse and select methods — to get the values of a dictionary and flatten the list.
fruits: list = [
    {"name":"apple", "price":[2,5]},
    {"name":"orange", "price":7},
    {"name":"grape", "price":3},
]
result_list: list = list(fruits | select(lambda  fruit: fruit["price"]) | traverse)
print(f"{result_list = }")
