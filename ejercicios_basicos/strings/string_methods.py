"""_summary_

    String Methods.
    - capitalize 
    - casefold
    - center
    - count
    - encode
    - endwith
    - expandtabs
    - find
    - format
    - format_map
    - index
    - isalnum
    - isalpha
    - isascii
    - isdecimal
    - isdigit
    - isidentifier
    - isnumeric
    - isprintable
    - islower
    - isspace
    - isupper
    - istitle
    - join
    - ljust
    - lower
    - lstrip 
    - maketrans
    - partition
    - replace
    - rfind
    - rindex
    - rjust
    - rpartition
    - rsplit
    - rstrip
    - split
    - splitlines
    - startswith
    - strip
    - swapcase
    - title
    - translate
    - upper
    - zfill
    - removeprefix
    - removesuffix

"""

print(" ")
print("capitalize: Convert first character to upper case and rest lowercase".center(100, "-"))
name: str = "juan"
new_name: str = name.capitalize()
print(f"{name} --> {new_name}")

print(" ")
print("casefold: Convert string to lower case. More aggresive than lower()".center(100, "-"))
text_any: str = "New TeXT frOm AnyWHERE"
new_text: str = text_any.casefold()
print(f"{text_any} --> {new_text}")

print(" ")
print("center: Returns centred string using optional value as fill character. Space (" ") is default".center(100, "-"))
name: str = "Vani"
new_name: str = name.center(9,"_")
print(f"{name} --> {new_name}")

print(" ")
print("count: Return number of times value is in string. Optional parameters specify where to search in string".center(100, "-"))
text_any: str = "New Text from AnyWherE"
e_count: int = text_any.count("e")
print(f"{text_any} --> e - {e_count}")

print(" ")
print("encode: Return encoded version of string. Optional parameter encoding & errors specify encoding to use and error method".center(100, "-"))
text_any: str = "Mr Stær"
new_text = text_any.encode('ascii', 'ignore')
print(f"{text_any} --> {new_text}")

print(" ")
print("endswith: Return true if string ends with value".center(100, "-"))
name_text: str = "Vani"
end_found: bool = name_text.endswith("ni")
print(f"{name_text} --> {end_found}")

print(" ")
print("expandtabs: Set tab size of string to specified number of whitespaces. Default is 8".center(100, "-"))
text_any: str = "H\tT\tM\tL\tO\tK"
result_text: str = text_any.expandtabs(3)
print(f"{text_any} --> {result_text}")

print(" ")
print("find: Return position of value if found in string.".center(100, "-"))
print("-1 returned if string not found. 2 optional params specifying where to start & end search".center(100, "-"))
text_new: str = "Texto en el que se buscará con el metodo find"
result_search = text_new.find("buscar")
print(f"{text_new} --> {result_search}")

print(" ")
print("format: Format values in string".center(100, "-"))
text_new: str = "Python {} The {}".format("is", "best")
print(f"{text_new = }")
text_new: str = "Python {1} The {0}".format("best", "is")
print(f"{text_new = }")


print(" ")
print("format_map: Format values in string using map-based substitution".center(100, "-"))
values_to_use: dict = {
    'a': 'Python',
    'b': 'like'
}
text_new: str = "I {b} {a}".format_map(values_to_use)
print(f"{text_new = }")

print(" ")
print("index: Return position of value if found in string.".center(100, "-"))
print("Raise exception if not found. 2 optional params specifying where to start & end search".center(100, "-"))
new_text: str = "Texto en el que se buscará con el metodo index"
result_search: int = new_text.index("buscar")
print(f"{new_text} --> {result_search}")

print(" ")
print("isalnum: Return true if all string characters are alphanumeric".center(100, "-"))
game: str = "Cyberpunk2077"
result: bool = game.isalnum()
print(f"{game} --> {result}")

print(" ")
print("isalpha: Return true if all string characters are in alphabet".center(100, "-"))
user_name: str = "User2099"
is_alpha: bool = user_name.isalpha()
print(f"{user_name} --> {is_alpha}")

print(" ")
print("isascii: Return true if all string characters are ascii".center(100, "-"))
game: str = "Cyberpunk2099"
is_ascii: bool = game.isascii()
print(f"{game} --> {is_ascii}")

print(" ")
print("isdecimal: Return true if all string characters are decimals (0-9)".center(100, "-"))
print("Can work on Unicode. Only supports decimals".center(100, "-"))
text_any: str = '1234555'
is_decimal: bool = text_any.isdecimal()
print(f"{text_any} --> {is_decimal}")

print(" ")
print("isdigit: Return true if all string characters are digits".center(100, "-"))
text_any: str = "3443"
is_degit: bool = text_any.isdigit()
print(f"{text_any} --> {is_degit}")

print(" ")
print("isidentifier: Return true if string is an identifer.".center(100, "-"))
print("These can only contain alphanumeric chars & underscores & can't start with numbers".center(100, "-"))
text_any: str = "2088User"
is_identifier: bool = text_any.isidentifier()
print(f"{text_any} --> {is_identifier}")

print(" ")
print("isnumeric: Return true if all characters are numeric".center(100, "-"))
number_text: str = "45973"
is_numeric: bool = number_text.isnumeric()
print(f"{number_text} --> {is_numeric}")

print(" ")
print("isprintable: Return true if all characters are printable".center(100, "-"))
text_any: str = "Hey\nMy name is Juan"
is_printable: bool = text_any.isprintable()
print(f"{text_any} --> {is_printable}")

print(" ")
print("islower: Return true if all characters are lower case".center(100, "-"))
name_text: str = "nombre_minusculas"
is_lower: bool = name_text.islower()
print(f"{name_text} --> {is_lower}")

print(" ")
print("isspace: Return true if all characters are whitespaces".center(100, "-"))
text_any: str = "  "
is_space: bool = text_any.isspace()
print(f"{text_any} --> {is_space}")

print(" ")
print("isupper: Return true if all characters are upper case".center(100, "-"))
text_any: str = "TODO EL TEXTO EN MAYUSCULAS"
is_upper: bool = text_any.isupper()
print(f"{text_any} --> {is_upper}") 

print(" ")
print("".center(100, "-"))

print(" ")
print("".center(100, "-"))

print(" ")
print("".center(100, "-"))

print(" ")
print("".center(100, "-"))

print(" ")
print("".center(100, "-"))

print(" ")
print("".center(100, "-"))

print(" ")
print("".center(100, "-"))

print(" ")
print("".center(100, "-"))

print(" ")
print("".center(100, "-"))



