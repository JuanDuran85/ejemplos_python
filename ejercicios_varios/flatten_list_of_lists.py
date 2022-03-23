from itertools import chain

numbers = [[1],[2,3],[4,[5,6,[7,8,[9,[10,11,12]]]]]]

# In this case, the itertools.chain methods only flatten the first level of a list of lists, that is, the method only goes down one level..
print(f"{list(chain.from_iterable(numbers))}")

# But, if you use recursion, you can drill down into the list of lists.
def flatten(lists_numbers):
    for num in lists_numbers:
        if isinstance(num, int):
            yield num
        else:
            yield from flatten(num)
            
result_list = list(flatten(numbers))
print(f"{result_list = }")
print(f"{sum(result_list) = }")

#Flattening a List: To flatten or spread a list that contains other lists of variable lengths and numbers, we can use the append() and extend() methods and keep adding that to the new list. The difference between the two methods is that append() adds a single variable to the end of the list such that the length of the list increases by one whereas extends() adds all the elements in the list passed as argument one by one to the end of the original list.

ugly_list: list = [10,12,36,[41,59,63],[77],81,93]
print(f"{ugly_list = }")
flat: list = []
for i in ugly_list:
    if isinstance(i, list):
        flat.extend(i)
    else:
        flat.append(i)
print(f"{flat = }")