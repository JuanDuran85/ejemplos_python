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