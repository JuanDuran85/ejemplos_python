"""[summary]

Using namedtuple is way shorter than defining a class manually
Using Counter to count the characters in a string. A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values. Counts are allowed to be any integer value including zero or negative counts. The Counter class is similar to bags or multisets in other languages.


"""

from collections import namedtuple, Counter

Car = namedtuple('Car', 'mileage color mark')

my_car = Car(80, 'Red', 'Audi')
print(f"{my_car =}")
print(f"{my_car.color = } , {my_car.mark = }")

# ------------------------------------------------------------------------
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