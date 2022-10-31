"""_summary_

    Interview Questions with code solutions

"""
# --------------------------------------------------------------------------------------
# Question 1 - Get missing number in [1...100], create a function and deleted 1 number
def get_missing_number(list_number: list) -> set:
    return set(range(list_number[-1])[1:]) - set(list_number)

list_number_any: list = list(range(1,100))
list_number_any.remove(45)
list_number_any.remove(5)
list_number_any.remove(33)
print(f"Missing number: {list(get_missing_number(list_number_any))}")

# --------------------------------------------------------------------------------------
# Question 2 - Find duplicate number in integer list
def find_duplicate_elements(elements) -> list:
    duplicates, seen = set(), set()
    for element in elements:
        if element in seen:
            duplicates.add(element)
        seen.add(element)
    return list(duplicates)

integer_list: list = [3,5,6,6,8,9,1,2,6,7,5,4,6,7]
print(f"duplicates elements: {find_duplicate_elements(integer_list)}")

# --------------------------------------------------------------------------------------
# Question 3 - Check if two strings are anagrams
def is_anagram(text_one: str, text_two: str) -> bool:
    return set(text_one.lower()) == set(text_two.lower())
print(f"is_anagram('elvis', 'lives'): {is_anagram('elvis', 'lives')}")

# --------------------------------------------------------------------------------------
# Question 4 - Check if a string is a palindrome
def is_palindrome(text_in: str) -> bool:
    return text_in == text_in[::-1]
print(f"is_palindrome('racecar'): {is_palindrome('racecar')}")

# --------------------------------------------------------------------------------------
# Question 5 - What's the difference between:

x = [i**2 for i in range(10)]
print(f"{x = }")
y = (i**2 for i in range(10))
print(f"{y = }")
print(next(y))
print(next(y))
print(next(y))

# X and Y hace the same values, but, they aren't interchanngeable, becouse Y is a generator
# ---------------------------------------------------------------------------------------