"""[summary]

Using namedtuple is way shorter than defining a class manually. Namedtuple create a __repr__ method

Using Counter to count the characters in a string. A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.

A ChainMap groups multiple dicts or other mappings together to create a single, updateable view. If no maps are specified, a single empty dictionary is provided so that a new chain always has at least one mapping.

defaultdict return a new dictionary-like object. defaultdict is a subclass of the built-in dict class. It overrides one method and adds one writable instance variable.

"""

from collections import OrderedDict, namedtuple, Counter, ChainMap, defaultdict

Car = namedtuple('Car', 'mileage color mark')

my_car = Car(80, 'Red', 'Audi')
print(f"{my_car =}")
print(f"{my_car.color = } , {my_car.mark = }")

Person = namedtuple('Person', ['name','last_name','age'])
person_one: Person = Person('Maria','Petronila','24')
print(f"{person_one = }")
print(f"{person_one[0] = }")
print(f"{person_one[1] = }")

# convert to tuples
print(tuple(person_one))
# unpacking
name, last_name, age = person_one
print(f"{name = } , {last_name = }, {age = }")
print(*person_one)

# subclassing from Person with namedtuple

class SubPerson(Person):
    def upper_case(self) -> str:
        return f"{self.name.upper()} {self.last_name.upper()}"
    
person_two: SubPerson = SubPerson("Juan","Perez","25")
print(person_two.upper_case())

# other way to create extendsion of namedtuple classes
SubPersonThree = namedtuple('SubPersonThree',Person._fields + ('email',))
person_three: SubPersonThree = SubPersonThree("Li","Xi","45","lixi@email.com")
print(f"{person_three}")

# convert to dictionary with asdict method (built-in)
dict_person_three: dict = person_three._asdict()
print(f"{dict_person_three = }")

# -------------------------------------------------------------------------------------

# Using Counter

count_in_string: Counter = Counter('paralelepipedo')
print(f"{count_in_string = }")
print(f"{count_in_string['p'] = }")
print(f"{sorted(count_in_string.elements()) = }")
print(f"{count_in_string.most_common(2) = }")
# para la version 3.10 ----> print(f"{count_in_string.total() = }")

count_in_dict: Counter = Counter({'red': 4, 'blue': 2})
print(f"{count_in_dict = }")
print(f"{count_in_dict['red'] = }")

count_in_keyword_args: Counter = Counter(a=4, b=2, c=0, d=-2)
print(f"{sorted(count_in_keyword_args.elements()) = }")

conteador_numeros_lista: Counter = Counter([1,1,2,2,3,3,3,3,4,4,5,5,5,6,7,8,9,9,9])
print(f"{conteador_numeros_lista = }")
print(f"{conteador_numeros_lista.most_common(1) = }")
print(f"{conteador_numeros_lista.most_common(2) = }")

# -------------------------------------------------------------------------------------
# Using ChainMap: Using ChainMap spares us from using a lot of conditional statements to check if a key is present in each of the dictionaries.

car_parts: dict = {
    'hood': 500,
    'engine': 5000,
    'front_door': 750
}

car_options: dict = {
    'A/C': 1000,
    'Turbo': 2500,
    'rollbar': 300
}

car_accessories: dict = {
    'cover': 100,
    'hood_ornament': 150,
    'seat_cover': 99
}

car_pricing: ChainMap = ChainMap(car_parts, car_options, car_accessories)
print(f"{car_pricing = }")
print(f"{car_pricing['A/C'] = }")

# -------------------------------------------------------------------------------------
# Using defaultdict

data: str = """Tim,ID
Sara,BR
Thelma,CN
Chris,RU
Fina,ID
Juliana,SE
Roberto,CN
Mario,PL
Paul,CN"""

countries = defaultdict(list)
for line in data.splitlines():
    name, country_code = line.split(',')
    countries[country_code].append(name)
print(f"{countries = }")
print(f"{countries['CN'] = }")

# -------------------------------------------------------------------------------------
# Using dOrderedDict: OrderedDict is commonly used whenever we want to keep the order in which the items are inserted into our dictionary.

ordered_dict: OrderedDict = OrderedDict()
ordered_dict['red'] = 0
ordered_dict['green'] = 3
ordered_dict['blue'] = 9
ordered_dict['yellow'] = 2
print(f"{ordered_dict = }")

del ordered_dict['red']
print(f"{ordered_dict = }")
ordered_dict['red'] = 0

ordered_dict.move_to_end('red')
print(f"{ordered_dict = }")

pop_item_dict = ordered_dict.popitem()
print(f"{pop_item_dict = }")
print(f"{ordered_dict = }")

# -------------------------------------------------------------------------------------
# Using defaultdict with lambda function to generate a default value

default_dict: defaultdict = defaultdict(lambda: 'Error Key - Not Found')
default_dict['a'] = 3   # type: ignore
default_dict['c'] = 6   # type: ignore
default_dict['f'] = 1   # type: ignore
default_dict['w'] = -9  # type: ignore
print(default_dict.items())
print(default_dict['a'])
print(default_dict['z'])

# -------------------------------------------------------------------------------------
# Using defaultdict with lambda function to generate a default value in a list

default_dict_list: defaultdict = defaultdict(list)
default_dict_list['names'].append('Maria')
default_dict_list['names'].append('Karla')
default_dict_list['names'].append('Juan')
print(default_dict_list)
print(default_dict_list.items())
print(default_dict_list.keys())
print(default_dict_list.values())

# -------------------------------------------------------------------------------------
# Searching data in multiple dictionaries as a single dictionary

dict_one: dict = {
    'one': 1,
    'two': 2,
    'three': 3
}

dict_two: dict = {
    'four': 4,
    'five': 5,
    'six': 6
}

combinational_dict: ChainMap = ChainMap(dict_one, dict_two)
print(f"{combinational_dict}")

# search starts from left to right
print(f"{combinational_dict['one'] = }")

# -------------------------------------------------------------------------------------
# You can use Counter methods to create a dict with the counts of numbers
# -------------------------------------------------------------------------------------
list_num: list[int] = [5,6,2,5,6,7,6,7,2,1,2,7,1,6,5]
cuenta:Counter[int] = Counter(list_num)
print(dict(cuenta))
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------