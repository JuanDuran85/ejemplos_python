"""_summary_

    Using pipe library.
    
    Pipe is a Python library that enables you to use pipes in Python. A pipe ( | ) passes the results of one method to another method. Pipe only provides a few methods.
    
    You can insert one method after another method using pipes. As a result, using
    pipes removes nested parentheses and makes the code more readable.

"""

from pipe import select, where, chain, traverse, groupby, dedup

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

# Group Elements in a List: we use groupby to group numbers into the Even group and the Odd group
list_number: list = [1,2,3,4,5,6,7,8,9,10,11,12]
resul_list: list = list(list_number | groupby(lambda num: "Par" if num%2==0 else "Impar") | select(lambda x: {x[0] : list(x[1])}))
print(f"{resul_list = }")

# To get only the values that are greater than 2, we can add the where method inside the select method.
new_result_list: list = list(list_number | groupby(lambda num: "Par" if num%2==0 else "Impar") | select(lambda num: {num[0]: list(num[1] | where(lambda num: num > 2))}))
print(f"{new_result_list = }")

# dedup — Deduplicate Values Using a Key. The dedup method removes duplicates in a list.
list_number: list = [3,3,4,6,3,5,7,3,2,4,3,6,3,5]
result_not_duplicate: list = list(list_number | dedup)
print(f"{result_not_duplicate = }")

# you can use the dedup method to get a unique element that is smaller than 5 and another unique element that is larger than or equal to 5.
new_result_not_duplicate: list = list(list_number | dedup(lambda key: key < 5))
print(f"{new_result_not_duplicate = }")

#In the code above, you can remove items with the same name, get the values of count, only choose the values that are integers.
data_list: list = [
    {"name":"Jack", "count": 4},
    {"name":"Isabel", "count": 1},
    {"name":"Joshuah", "count": None},
    {"name":"Isabel", "count": 3},
    {"name":"Kody", "count": 8},
    {"name":"Joshuah", "count": 2},
]

result_data: list = list(data_list | dedup(key=lambda person: person["name"]) | select(lambda person: person["count"])| where(lambda count: isinstance(count, int)))
print(f"{result_data = }")