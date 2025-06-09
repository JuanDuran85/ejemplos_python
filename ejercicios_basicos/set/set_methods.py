# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

"""_summary_

    Python Set Methods.
    
    - add
    - pop
    - union
    - issuperset
    - issubset
    - intersection
    - difference
    - isdisjoint
    - discard
    - copy
    - difference_update
    - intersection_update
    - symmetric_difference
    - symmetric_difference_update
    - remove
    - clear
    
    
"""

print(" ")
set_items_one: set = {'a', 'b', 'c', 'd'}
print(f"{set_items_one=}")
set_items_two: set = {'x', 'y', 'z', 'w'}
print(f"{set_items_two=}")
set_items_three: set = {'b', 'c', 'h', 'a'}
print(f"{set_items_three=}")
set_items_four: set = {'d', 'b', 'x', 'p'}
print(f"{set_items_four=}")
set_items_five: set = {'e', 'd', 'p', 'a'}
print(f"{set_items_five=}")

print(" ")
print("ADD: Adds an element to the set".center(100, "-"))
set_items_one.add('e')
print(f"{set_items_one=}")

print(" ")
print("POP: The pop() method removes a random item from the set.".center(100, "-"))
print("This method returns the removed item.".center(100, "-"))
delete_item = set_items_one.pop()
print(f"{delete_item=}")
print(f"{set_items_one=}")

print(" ")
print("UNION: Return a set containing the union of sets".center(100, "-"))
result_union_set_one = set_items_one.union(set_items_two)
print(f"{result_union_set_one=}")
result_union_set_two = set_items_one.union(set_items_three)
print(f"{result_union_set_two=}")
result_union_set_three = set_items_one | set_items_three
print(f"{result_union_set_three=}")

print(" ")
print("ISSUPERSET:  returns True if a set has every elements of another set".center(100, "-"))
print("If not, it returns False.".center(100, "-"))
super_set: bool = set_items_one.issuperset(set_items_two)
print(f"{super_set=}")

print(" ")
print("ISSUBSET: Return True if all items in set x are present in set y:".center(100, "-"))
sub_set: bool = set_items_one.issubset(set_items_two)
print(f"{sub_set=}")

print(" ")
print("INTERSECTION: Returns a set, that is the intersection of two or more sets".center(100, "-"))
new_set_inter: set = set_items_one.intersection(set_items_three)
print(f"{new_set_inter=}")

print(" ")
print("DIFFERENCE: Returns a set containing the difference between two or more sets".center(100, "-"))
new_set_dif: set = set_items_one.difference(set_items_three)
print(f"{new_set_dif=}")

print(" ")
print("ISDISJOINT: Returns whether two sets have a intersection or not".center(100, "-"))
new_set_disj: bool = set_items_one.isdisjoint(set_items_two)
print(f"{new_set_disj=}")

print(" ")
print("DISCARD: Remove the specified item from the set".center(100, "-"))
print("This method will not raise an error if the specified item does not exist".center(100, "-"))
set_items_three.discard('a')
print(f"{set_items_three=}")

print(" ")
print("COPY: Returns a copy of the set".center(100, "-"))
copy_set: set = set_items_two.copy()
print(f"{copy_set=}")

print(" ")
print("DIFFERENCE_UPDATE: removes the items that exist in both sets.".center(100, "-"))
set_items_four.difference_update(set_items_five)
print(f"{set_items_four=}")

print(" ")
print("INTERSECTION_UPDATE: removes the items that is not present in both sets".center(100, "-"))
print("or in all sets if the comparison is done between more than two sets".center(100, "-"))
set_items_one.intersection_update(set_items_five)
print(f"{set_items_one=}")

print(" ")
print("SYMMETRIC_DIFFERENCE_UPDATE: updates the original set by removing items".center(100, "-"))
print("that are present in both sets, and inserting the other items.".center(100, "-"))
set_items_four.symmetric_difference_update(set_items_five)
print(f"{set_items_four=}")

print(" ")
print("SYMMETRIC_DIFFERENCE: returns a set that contains all items from both set".center(100, "-"))
print("but not the items that are present in both sets.".center(100, "-"))
print(f"{set_items_one=}")
print(f"{set_items_two=}")
new_set_sd: set = set_items_one.symmetric_difference(set_items_two)
print(f"{new_set_sd=}")

print(" ")
print("REMOVE: method removes the specified element from the set.".center(100, "-"))
print("This method will raise an error if the specified item does not exist".center(100, "-"))
set_items_five.remove('a')
print(f"{set_items_five=}")

print(" ")
print("CLEAR: Removes all the elements from the set".center(100, "-"))
set_items_one.clear()
print(f"{set_items_one=}")
