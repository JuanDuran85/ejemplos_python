# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103


# sourcery skip: dict-assign-update-to-union
"""_summary_

    Python Dictionary Methods.
    
    - clear
    - copy
    - fromkeys
    - get
    - items
    - keys
    - pop
    - popitem
    - setdefault
    - update
    - values
    
"""

LINES = "---------------------------------------------------------------------\r"


print(LINES)
print(" ")
print("CLEAR: Remove all elements from Dictionary".center(100, "-"))
food: dict[int, str] = {
    1: "Pizza",
    2: "Hamburgs",
}
print(f"Dictionary: {food}")
food.clear()
print(f"{food=}")

print(LINES)
print(" ")
print("COPY: Return copy of Dictionary".center(100, "-"))
cities: dict[int, str] = {
    1: "Madrid",
    2: "Roma",
    3: "Santiago de Chile",
    4: "Paris",
    5: "Sao Paulo",
}
print(f"Dictionary: {cities}")
cities_two: dict[int, str] = cities.copy()
print(f"{cities_two=}")

print(LINES)
print(" ")
print("FROMKEYS: Return Dictionary with specified keys & values.".center(100, "-"))
print("Optional Parameter: Value. This is what's set for all keys. Default is None".center(100, "-"))
key: tuple = ("Spain", "Italy", "Chile", "France", "Brazil")
value: str = "Country"
countries: dict = dict.fromkeys(key, value)
print(f"Dictionary: {countries}")

print(LINES)
print(" ")
print("GET: Return value of specified key.".center(100, "-"))
print("Optional Parameter: Value. Value returned if no key exists. Default is None".center(100, "-"))
cities_three: dict[int, str] = {
    1: "Madrid",
    2: "Roma",
    3: "Santiago de Chile",
    4: "Paris",
    5: "Sao Paulo",
}
print(f"Dictionary: {cities_three}")
get_value_dict: str | None = cities_three.get(3)
print(f"{get_value_dict=}")

# Using the .get() method on the dictionary instead of using [”key”] allows
# to streamline dictionary lookups for items that may not exist.

city_number_six: str = cities_three.get(6, 'City not found')
print(f"{city_number_six=}")


print(LINES)
print(" ")
print("ITEMS: Return view object containing list of key value pairs.".center(100, "-"))
food_two: dict = {
    1: "Pizza",
    2: "Hamburgs",
}
print(f"Dictionary: {food_two}")
items_food = food_two.items()
print(f"{items_food=}")

print(LINES)
print(" ")
print("KEYS: Return view object containing list of keys".center(100, "-"))
cities_four: dict = {
    1: "Madrid",
    2: "Roma",
    3: "Santiago de Chile",
    4: "Paris",
    5: "Sao Paulo",
}
print(f"Dictionary: {cities_four}")
keys_cities = cities_four.keys()
print(f"{keys_cities=}")

print(LINES)
print(" ")
print("POP: Remove element with specified key and return it.".center(100, "-"))
print("Optional Parameter: Default value. This is value to return if no key is found in dictionary".center(100, "-"))
food_three: dict = {
    1: "Pizza",
    2: "Hamburgs",
    3: "Chicken",
}
print(f"Dictionary: {food_three}")
pop_value: str = food_three.pop(2)
print(f"{pop_value=}")
print(f"{food_three=}")

print(LINES)
print(" ")
print("POPITEM: Remove last inserted key value pair and return as tuple.".center(100, "-"))
print("Python < 3.7 method returns random item".center(100, "-"))
cities_five: dict = {
    1: "Madrid",
    2: "Roma",
    3: "Santiago de Chile",
    4: "Paris",
    5: "Sao Paulo",
}
print(f"Dictionary: {cities_five}")
popitem_value: tuple = cities_five.popitem()
print(f"{popitem_value=}")
print(f"{cities_five=}")

print(LINES)
print(" ")
print("SETDEFAULT: Return value of item with specified key. If key doesn't exist, insert with specified value.".center(100, "-"))
print("Optional Parameter: value. Default is None".center(100, "-"))
food_four: dict = {
    1: "Pizza",
    2: "Hamburgs",
    3: "Chicken",
}
print(f"Dictionary: {food_four}")
set_default_food_exist: str | None = food_four.setdefault(2, 'Food')
print(f"{set_default_food_exist=}")
set_default_food_noexist: str = food_four.setdefault(4, "Soup")
print(f"{set_default_food_noexist=}")
print(f"{food_four=}")

print(LINES)
print(" ")
print("UPDATE: Update dictionary with specified key value pairs".center(100, "-"))
cities_four: dict = {
    1: "Madrid",
    2: "Roma",
    3: "Santiago de Chile",
    4: "Paris",
    5: "Sao Paulo",
}
print(f"Dictionary: {cities_four}")
cities_four.update({6: "Caracas", 7: "Lisbon"})
print(f"{cities_four=}")

print(LINES)
print(" ")
print("VALUES: Return view objects containing list of values.".center(100, "-"))
food_five: dict = {
    1: "Pizza",
    2: "Hamburgs",
    3: "Chicken",
}
print(f"Dictionary: {food_five}")
values_dict = food_five.values()
print(f"{values_dict=}")

print(LINES)
