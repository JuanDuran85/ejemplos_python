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

print(" ")
print("CLEAR: Remove all elements from Dictionary".center(100, "-"))
food: dict = {
    1: "Pizza",
    2: "Hamburguesa",
}
print(f"Dictionary: {food}")
food.clear()
print(f"{food = }")

print(" ")
print("COPY: Return copy of Dictionary".center(100, "-"))
cities: dict = {
    1: "Madrid",
    2: "Roma",
    3: "Santiago de Chile",
    4: "Paris",
    5: "Sao Paulo",
}
print(f"Dictionary: {cities}")
cities_two: dict = cities.copy()
print(f"{cities_two = }")

print(" ")
print("FROMKEYS: Return Dictionary with specified keys & values.".center(100, "-"))
print("Optional Parameter: Value. This is what's set for all keys. Default is None".center(100, "-"))
key: tuple = ("España","Italia","Chile","Francia","Brasil")
value: str = "Country"
countries: dict = dict.fromkeys(key, value)
print(f"Dictionary: {countries}")

print(" ")
print("GET: Return value of specified key.".center(100, "-"))
print("Optional Parameter: Value. Value returned if no key exists. Default is None".center(100, "-"))
cities: dict = {
    1: "Madrid",
    2: "Roma",
    3: "Santiago de Chile",
    4: "Paris",
    5: "Sao Paulo",
}
print(f"Dictionary: {cities}")
get_value_dict: str | None = cities.get(3)
print(f"{get_value_dict = }")

print(" ")
print("ITEMS: Return view object containing list of key value pairs.".center(100, "-"))
food: dict = {
    1: "Pizza",
    2: "Hamburguesa",
}
print(f"Dictionary: {food}")
items_food = food.items()
print(f"{items_food = }")

print(" ")
print("KEYS: Return view object containing list of keys".center(100, "-"))
cities: dict = {
    1: "Madrid",
    2: "Roma",
    3: "Santiago de Chile",
    4: "Paris",
    5: "Sao Paulo",
}
print(f"Dictionary: {cities}")
keys_cities = cities.keys()
print(f"{keys_cities = }")

print(" ")
print("POP: Remove element with specified key and return it.".center(100, "-"))
print("Optional Parameter: Defaultvalue. This is value to return if no key is found in dictionary".center(100, "-"))
food: dict = {
    1: "Pizza",
    2: "Hamburguesa",
    3: "Pollo",
}
print(f"Dictionary: {food}")
pop_value: str = food.pop(2)
print(f"{pop_value = }")
print(f"{food = }")

print(" ")
print("POPITEM: Remove last inserted key value pair and return as tuple.".center(100, "-"))
print("Python < 3.7 method returns random item".center(100, "-"))
cities: dict = {
    1: "Madrid",
    2: "Roma",
    3: "Santiago de Chile",
    4: "Paris",
    5: "Sao Paulo",
}
print(f"Dictionary: {cities}")
popitem_value: tuple = cities.popitem()
print(f"{popitem_value = }")
print(f"{cities = }")

print(" ")
print("SETDEFAULT: Return value of item with specified key. If key doesn't exist, insert with specified value.".center(100, "-"))
print("Optional Parameter: value. Default is None".center(100, "-"))
food: dict = {
    1: "Pizza",
    2: "Hamburguesa",
    3: "Pollo",
}
print(f"Dictionary: {food}")
set_default_food_exist: str | None = food.setdefault(2,'Comida')
print(f"{set_default_food_exist = }")
set_default_food_noexist: str = food.setdefault(4, "Sopa")
print(f"{set_default_food_noexist = }")
print(f"{food = }")

print(" ")
print("UPDATE: Update dictionary with specified key value pairs".center(100, "-"))
cities: dict = {
    1: "Madrid",
    2: "Roma",
    3: "Santiago de Chile",
    4: "Paris",
    5: "Sao Paulo",
}
print(f"Dictionary: {cities}")
cities.update({6: "Caracas", 7: "Lisboa"})
print(f"{cities = }")

print(" ")
print("VALUES: Return view objects containing list of values.".center(100, "-"))
food: dict = {
    1: "Pizza",
    2: "Hamburguesa",
    3: "Pollo",
}
print(f"Dictionary: {food}")
values_dict = food.values()
print(f"{values_dict = }")