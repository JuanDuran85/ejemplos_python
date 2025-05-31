"""_summary_

    String Methods.
    - capitalize 
    - casefold
    - center
    - count
    - encode
    - endswith
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
new_name: str = name.center(9, "_")
print(f"{name} --> {new_name}")

print(" ")
print("count: Return number of times value is in string. Optional parameters specify where to search in string".center(100, "-"))
text_any: str = "New Text from AnyWherE"
e_count: int = text_any.count("e")
print(f"{text_any} --> e - {e_count}")

print(" ")
print("encode: Return encoded version of string. Optional parameter encoding & errors specify encoding to use and error method".center(100, "-"))
text_any: str = "Mr Stær"
new_text = text_any.encode('ascii', 'ignore')  # type: ignore
print(f"{text_any} --> {new_text}")

print(" ")
print("endswith: Return true if string ends with value".center(100, "-"))
name_text: str = "Vani"
end_found: bool = name_text.endswith("ni")
print(f"{name_text} --> {end_found}")

print(" ")
print("expandtabs: Set tab size of string to specified number of whitespaces. Default is 8".center(100, "-"))
text_any: str = "H\tT\tM\tL\tO\tK"
result_text_four: str = text_any.expandtabs(3)
print(f"{text_any} --> {result_text_four}")

print(" ")
print("find: Return position of value if found in string.".center(100, "-"))
print("-1 returned if string not found. 2 optional params specifying where to start & end search".center(100, "-"))
text_new: str = "Texto en el que se buscará con el metodo find"
result_search = text_new.find("buscar")
print(f"{text_new} --> {result_search}")

print(" ")
print("format: Format values in string".center(100, "-"))
text_new: str = "Python {} The {}".format("is", "best")
print(f"{text_new=}")
text_new: str = "Python {1} The {0}".format("best", "is")
print(f"{text_new=}")


print(" ")
print("format_map: Format values in string using map-based substitution".center(100, "-"))
values_to_use: dict = {
    'a': 'Python',
    'b': 'like'
}
text_new: str = "I {b} {a}".format_map(values_to_use)
print(f"{text_new=}")

print(" ")
print("index: Return position of value if found in string.".center(100, "-"))
print("Raise exception if not found. 2 optional params specifying where to start & end search".center(100, "-"))
new_text: str = "Texto en el que se buscará con el metodo index"
result_search: int = new_text.index("buscar")
print(f"{new_text} --> {result_search}")

print(" ")
print("isalnum: Return true if all string characters are alphanumeric".center(100, "-"))
game: str = "Cyberpunk2077"
result_isalnum: bool = game.isalnum()
print(f"{game} --> {result_isalnum}")

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
print("istitle: Return true if string follows rules of a title".center(100, "-"))
print("if all words are lowercase except the first letter of each word".center(100, "-"))
title_text: str = "Titulo Nuevo De La Pagina"
is_title: bool = title_text.istitle()
print(f"{title_text} --> {is_title}")


print(" ")
print("join: Join iterable elements to end of stiring".center(100, "-"))
cadena_uno: tuple = ("texto 1", "texto 2", "texto 3")
result_text_four: str = "__".join(cadena_uno)
print(f"{cadena_uno} --> {result_text_four}")

print(" ")
print("ljust: Return string left justified".center(100, "-"))
print("2nd optional param specifies character to fill space. Default is space".center(100, "-"))
text_any: str = "Python 3.10"
result: str = text_any.ljust(20, "*")
print(f"{text_any} --> {result}")

print(" ")
print("lower: Convert string to lower case".center(100, "-"))
text_any: str = "TODO EL TEXTO EN MAYUSCULAS"
lower_text: str = text_any.lower()
print(f"{text_any} --> {lower_text}")

print(" ")
print("lstrip: Same as strip but only leading chars".center(100, "-"))
text_any: str = "   Python 3.10          "
result_text__five: str = text_any.lstrip()
print(f"{text_any} --> {result_text__five}")

print(" ")
print("maketrans: Return translation table that can be used with translate()".center(100, "-"))
text_any: str = "Harry Cotter"
result_change: dict = text_any.maketrans("C", "P")
print(f"{text_any} --> {text_any.translate(result_change)}")

print(" ")
print("partition: Return tuple with string parted in 3 parts".center(100, "-"))
print("Middle part is specified string. If not found, entire string stored in first part of tuple".center(100, "-"))
text_any: str = "Program Language Python 3.10"
result_text_two: tuple = text_any.partition('Language')
print(f"{text_any} --> {result_text_two}")

print(" ")
print("replace: Return string where one value is replaced with another".center(100, "-"))
print("Optional parameter specifies how many occurrences to replace".center(100, "-"))
text_any: str = "Texto que esta estatico una vez"
result_text_three: str = text_any.replace('estatico', 'remplazado')
print(f"{text_any} --> {result_text_three}")

print(" ")
print("rfind: Same as find but searches for last occurrence of string".center(100, "-"))
text_any: str = "Texto que se usa para busqueda con rfind"
result_search: int = text_any.rfind('xxx')
print(f"{text_any} --> {result_search}")

print(" ")
print("rindex: Same as index but searches for last occurence of string".center(100, "-"))
text_any: str = "It's alive!!! It's alive!!!"
result_search: int = text_any.rindex('alive')
print(f"{text_any} --> {result_search}")

print(" ")
print("rjust: Return string right justified.".center(100, "-"))
print("2nd optional param specifies character to fill space. Default is space.".center(100, "-"))
text_any: str = "Texto a justificar"
r_just_text: str = text_any.rjust(50, ".")
print(f"{r_just_text}")

print(" ")
print("rpartition: Same as partition but searches for last occurence of string".center(100, "-"))
text_any: str = "One for you and one for me"
r_partition: tuple = text_any.rpartition('for')
print(f"{text_any} --> {r_partition}")

print(" ")
print("rsplit: Same as split but starts from the right".center(100, "-"))
text_any: str = "One for you and one for me"
result_text: list[str] = text_any.rsplit('for')
print(f"{text_any} --> {result_text}")

print(" ")
print("rstrip: Same as strip but only trailing chars".center(100, "-"))
text_any: str = "    Python 3.10          "
r_strip_result: str = text_any.rstrip()
print(f"{text_any} --> {r_strip_result} !!!")

print(" ")
print("split: Split string at whitespace and return list".center(100, "-"))
print("2 optional params allow you to specify separator and how many splits to do.".center(100, "-"))
text_any: str = "No! No! No! No! No! No! No!"
result_split: list = text_any.split('! ', 3)
print(f"{text_any} --> {result_split}")

print(" ")
print("splitlines: Split string at linebreaks and return list".center(100, "-"))
print("Optional param determines whether to include line break after split".center(100, "-"))
text_any: str = "Line 1\nLine 2\nLine 3"
result_splitlines: list = text_any.splitlines()
print(f"{text_any} --> {result_splitlines}")

print(" ")
print("startswith: Return true if string starts with value".center(100, "-"))
name_text: str = "Maria"
starts_with: bool = name_text.startswith("M")
print(f"{name_text} --> {starts_with}")

print(" ")
print("strip: Remove leading & trailing chars".center(100, "-"))
print("Optional param specifies chars to remove as leading/trailing chars".center(100, "-"))
text_any: str = "   Espacios en blanco   "
result_strip: str = text_any.strip()
print(f"{text_any} --> {result_strip}!!!")

print(" ")
print("swapcase: Swap cases (e.g. lowercase become upper)".center(100, "-"))
text_any: str = "e.t PHONE HOME"
swapcase_result: str = text_any.swapcase()
print(f"{text_any} --> {swapcase_result}")

print(" ")
print("title: Covert first character of each word to upper case".center(100, "-"))
text_title: str = "este titulo fue cambiado con title"
result_title: str = text_title.title()
print(f"{text_title} --> {result_title}")

print(" ")
print("translate: Returns a translated string using mapping table, or dictionary with ascii characters".center(100, "-"))
text_ascii: dict = {74: 80, 105: 97}
result_translate: str = "Joe".translate(text_ascii)
print(f"{text_ascii} --> {result_translate}")

print(" ")
print("upper: Convert characters to uppercase".center(100, "-"))
text_any: str = "TeXto CuAlQuieRa stRing"
result_upper: str = text_any.upper()
print(f"{text_any} --> {result_upper}")

print(" ")
print("zfill: Fills string with specified number of 0 values at start".center(100, "-"))
price_article: str = ".125"
price_fill: str = price_article.zfill(5)
print(f"{price_article} --> {price_fill}")

print(" ")
print("removeprefix: Return string without specified prefix. Only Python 3.9+".center(100, "-"))
name_text: str = "Aeron"
new_name = name_text.removeprefix("Ae")
print(f"{name_text} --> {new_name}")

print(" ")
print("removesuffix: Return string without specified suffix. Only Python 3.9+.".center(100, "-"))
name_text: str = "Aeron"
new_name = name_text.removesuffix("on")
print(f"{name_text} --> {new_name}")
