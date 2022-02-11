"""[summary]

Using namedtuple is way shorter than defining a class manually

"""

from collections import namedtuple

Car = namedtuple('Car', 'mileage color mark')

my_car = Car(80, 'Red', 'Audi')
print(f"{my_car =}")
print(f"{my_car.color = } , {my_car.mark = }")