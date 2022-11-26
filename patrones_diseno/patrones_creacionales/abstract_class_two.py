"""_summary_

    Abstraction is the concept in object-oriented programming that is used to hide the internal functionality of the classes from the users.
    
    Abstraction is implemented using the abstract classes. An abstract class in Python is typically created to declare a set of methods that must be created in any child class built on top of this abstract class. Similarly, an abstract method is one that doesn't have any implementation.

    Abstract methods force the child classes to give the implementation of these methods in them and thus help us achieve abstraction as each subclass can give its own implementation. A class containing more than one abstract method is called an abstract class.
    
    Properties are Pythonic ways of using getters and setters. The abc module has a @abstractproperty decorator to use abstract properties
    
    We cannot create an instance or object of an abstract class in Python. If we try to instantiate the abstract class, it raises an error.
    
    A Concrete class is a class that has a definition for all its methods and has no abstract method.

"""

from abc import ABC, abstractmethod, abstractproperty

class Shape(ABC):
    def __init__(self, shape_name):
        self.shape_name = shape_name
        
    @abstractproperty
    def name(self): ...
    
    @abstractmethod
    def draw(self):
        print(f"Preparing canvas for: {self.shape_name}")
    
class Circle(Shape):
    def __init__(self):
        super().__init__("Circle")
        
    @property
    def name(self):
        return self.shape_name
    
    def draw(self):
        super().draw()
        return f"drawing a {self.shape_name}"
    

class Triangle(Shape):
    def __init__(self):
        super().__init__("Triangulo")
        
    @property
    def name(self):
        return self.shape_name
        
    def draw(self):
        super().draw()
        return f"Drawing a {self.shape_name}"

# creating a circle
circ_one = Circle()
print(circ_one.draw())
print(f"The name is: {circ_one.name}")

# creating a triangle
trian_one = Triangle()
trian_one.shape_name = "Triangle"
print(trian_one.draw())
print(f"The name is: {trian_one.name}")