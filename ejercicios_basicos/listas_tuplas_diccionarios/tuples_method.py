"""_summary_

    Python Tuple Methods.
    
    - count
    - index
    
"""
tuple_one: tuple = (0,1,2,2,3,5,6,6,5,3,2,1,2,3,4,5)
tuple_two: tuple = ("Maria","John","jose","Petra","Maria","Petra","Maria")
print(f"tuple_one: {tuple_one}")
print(f"tuple_two: {tuple_two}")

print(" ")
print("COUNT: Returns the number of times a specified value occurs in a tuple".center(100, "-"))
result_tuple: int = tuple_one.count(2)
print(f"The number of times the value 2 occurs in the tuple is: {result_tuple}")
result_tuple: int = tuple_two.count("Maria")
print(f"The number of times the value 'Maria' occurs in the tuple is: {result_tuple}")

print(" ")
print("INDEX: Searches the tuple for a specified value and returns the position of where it was found".center(100, "-"))
result_position: int = tuple_one.index(2)
print(f"The position of the value 2 in the tuple is: {result_position}")
result_position: int = tuple_two.index("Maria")
print(f"The position of the value 'Maria' in the tuple is: {result_position}")