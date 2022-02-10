from itertools import accumulate

"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using lists - Can be: ordered, mutable, duplicates'''
print("\n Using lists with itertools \n")

n_values_in_list_two = range(0,10,2)
print(f"{n_values_in_list_two = }")

# With accumulate from itertools librery, you can sum the values ​​in a list
print(f"{list(accumulate(n_values_in_list_two)) = }")