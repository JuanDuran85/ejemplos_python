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
    - setdiscard
    - copy
    - clear
    
"""

print(" ")
set_items_one: set = {'a','b','c','d'}
print(f"{set_items_one = }")
set_items_two: set = {'x','y','z','w'}
print(f"{set_items_two = }")
set_items_three: set = {'b','g','h','a'}
print(f"{set_items_three = }")

print(" ")
print("ADD: Adds an element to the set".center(100, "-"))
set_items_one.add('e')
print(f"{set_items_one = }")

print(" ")
print("POP: The pop() method removes a random item from the set.".center(100, "-"))
print("This method returns the removed item.".center(100, "-"))
delete_item = set_items_one.pop()
print(f"{delete_item = }")
print(f"{set_items_one = }")

print(" ")
print("UNION: Return a set containing the union of sets".center(100, "-"))
result_union_set_one = set_items_one.union(set_items_two)
print(f"{result_union_set_one = }")
result_union_set_two = set_items_one.union(set_items_three)
print(f"{result_union_set_two = }")
result_union_set_three = set_items_one | set_items_three
print(f"{result_union_set_three = }")

print(" ")
print("ISSUPERSET:  returns True if a set has every elements of another set".center(100, "-"))
print("If not, it returns False.".center(100, "-"))
super_set: bool = set_items_one.issuperset(set_items_two)
print(f"{super_set = }")

print(" ")
print("ISSUBSET: Return True if all items in set x are present in set y:".center(100, "-"))
sub_set: bool = set_items_one.issubset(set_items_two)
print(f"{sub_set = }")

print(" ")
print("INTERSECTION: Returns a set, that is the intersection of two or more sets".center(100, "-"))



print(" ")
print("DIFFERENCE: Returns a set containing the difference between two or more sets".center(100, "-"))



print(" ")
print("ISDISJOINT: Returns whether two sets have a intersection or not".center(100, "-"))



print(" ")
print("SETDISCARD: ".center(100, "-"))



print(" ")
print("COPY: Returns a copy of the set".center(100, "-"))



print(" ")
print("CLEAR: Removes all the elements from the set".center(100, "-"))
set_items_one.clear()
print(f"{set_items_one = }")