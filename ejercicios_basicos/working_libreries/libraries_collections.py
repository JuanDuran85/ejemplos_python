"""[summary]

Using namedtuple is way shorter than defining a class manually

Using Counter to count the characters in a string. A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.

A ChainMap groups multiple dicts or other mappings together to create a single, updateable view. If no maps are specified, a single empty dictionary is provided so that a new chain always has at least one mapping.

defaultdict return a new dictionary-like object. defaultdict is a subclass of the built-in dict class. It overrides one method and adds one writable instance variable.

"""

from collections import namedtuple, Counter, ChainMap, defaultdict

Car = namedtuple('Car', 'mileage color mark')

my_car = Car(80, 'Red', 'Audi')
print(f"{my_car =}")
print(f"{my_car.color = } , {my_car.mark = }")

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
# Using ChainMap

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
