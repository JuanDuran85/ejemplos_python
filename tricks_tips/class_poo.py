"""[summary]

Tips and tricks for class -POO in Python.

All the examples are in the same file, but they are separated with a mark

All examples are from the internet with somes variations, so they are not 100% correct. Thanks to the authors.

"""
"""----------------------------------------------------------------------------------------"""
"""----------------------------------------------------------------------------------------"""
''' Using inheritance'''
print("\n Using inheritance \n")

# If you need know one class is a subclass of another, you can use the issubclass method.
class Vehicle:
    def __init__(self, year, model):
        self.year = year
        self.model = model

class Car(Vehicle):
    def __init__(self, year, model, color):
        super().__init__(year, model)
        self.color = color
        
print(f"{issubclass(Car, Vehicle) = }")
print(f"{issubclass(Vehicle, Car) = }")

print("\n Using __len__ method \n")

# To get the length of the class, you can use the __len__ method.

class Cart:
    def __init__(self, item):
        self.item = item
    def __len__(self):
        return len(self.item)

c = Cart("Hello")
print(f"{len(c) = }")