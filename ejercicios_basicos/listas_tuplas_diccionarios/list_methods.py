"""_summary_

    Python List Methods.
    
    - append
    - clear
    - copy
    - count
    - extend
    - index
    - insert
    - pop
    - remove
    - reverse
    - sort
    
"""
print(" ")
print("APPEND: Add single element to end of list".center(100, "-"))
office: list = ["Juan", "Pedro", "Ana", "Maria"]
print(f"List: {office}")
office.append("Jorge")
print(f"{office = }")

print(" ")
print("CLEAR: Remove all Items from list".center(100, "-"))
office_two: list = ["Holly", "Kayla", "Liz", "Molly"]
print(f"List: {office_two}")
office_two.clear()
print(f"{office_two = }")

print(" ")
print("COPY: Return shallow copy of list".center(100, "-"))
office: list = ["Juan", "Pedro", "Ana", "Maria"]
print(f"List: {office}")
office_copy: list = office.copy()
print(f"{office_copy = }")

print(" ")
print("COUNT: Return count of an element in list".center(100, "-"))
office_two: list = ["Holly", "Kayla", "Liz", "Molly", "Holly"]
print(f"List: {office_two}")
count_holly: int = office_two.count("Holly")
print(f"{count_holly = }")

print(" ")
print("EXTEND: Adds iterable elements to end of list".center(100, "-"))
office: list = ["Juan", "Pedro", "Ana", "Maria"]
print(f"List: {office}")
office.extend(["Jorge", "Josefina"])
print(f"{office = }")

print(" ")
print("INDEX: Return index of first element in list matching given value".center(100, "-"))
office_two: list = ["Holly", "Kayla", "Liz", "Molly", "Holly"]
print(f"List: {office_two}")
index_of_holly: int = office_two.index("Holly")
print(f"{index_of_holly = }")

print(" ")
print("INSERT: Insert element to list at given index".center(100, "-"))
office: list = ["Juan", "Pedro", "Ana", "Maria"]
print(f"List: {office}")
office.insert(2, "Jorge")
print(f"{office = }")

print(" ")
print("POP: Remove element at given index and returns it, or remove the last element".center(100, "-"))
office_two: list = ["Holly", "Kayla", "Liz", "Molly", "Holly"]
print(f"List: {office_two}")
pop_element_1: str = office_two.pop(1)
print(f"{pop_element_1 = }")
print(f"{office_two = }")

print(" ")
print("REMOVE: Remove first item from list that has given value".center(100, "-"))
office: list = ["Juan", "Pedro", "Ana", "Maria", "Pedro"]
print(f"List: {office}")
office.remove("Pedro")
print(f"{office = }")

print(" ")
print("REVERSE: Reverse the list".center(100, "-"))
office_two: list = ["Holly", "Kayla", "Liz", "Molly", "Holly"]
print(f"List: {office_two}")
office_two.reverse()
print(f"{office_two = }")

print(" ")
print("SORT: Sort elements of a list".center(100, "-"))
office: list = ["Juan", "Pedro", "Ana", "Maria", "Pedro"]
print(f"List: {office}")
office.sort()
print(f"{office = }")