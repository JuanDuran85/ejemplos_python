"""
    The Factory Method is used in object-oriented programming as a means to provide factory interfaces for creating objects. These interfaces define the generic structure, but don't initialize objects. The initialization is left to more specific subclasses.
    
    The Factory Method design pattern is commonly used in libraries by allowing clients to choose what subclass or type of object to create through an abstract class.

    A Factory Method will receive information about a required object, instantiate it and return the object of the specified type. This gives our application or library a single point of interaction with other programs or pieces of code, thereby encapsulating our object creation functionality.

"""

from abc import ABCMeta, abstractmethod, ABC

PI: float = 3.1416

# First: we will start by creating an abstract class to represent a generic x object. This is the base class for all of our x objects.
class Shape(metaclass=ABCMeta):
    @abstractmethod
    def calcule_area(self): ...
    
    @abstractmethod
    def calcule_perimeter(self): ...
    
# Now: you can create several concrete, more specific x objects.
class Rectangule(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calcule_area(self):
        return (self.width * self.height)
    
    def calcule_perimeter(self):
        return (self.width + self.height) * 2
    
class Square(Shape):
    def __init__(self, width):
        self.width = width
        
    def calcule_area(self):
        return (self.width**2)
    
    def calcule_perimeter(self):
        return self.width * 4
    
class Circule(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def calcule_area(self):
        return PI * (self.radius**2)
    
    def calcule_perimeter(self):
        return (PI * self.radius * 2)    


# In order to create the different X objects, clients will have to know the names and details of our X objects and separately perform the creation.This is where the Factory Method comes into play. The Factory Method design pattern will help us abstract the available X objects from the client.

class ShapeFactory:
    @classmethod
    def __rectangule_creation(cls):
        width = input("Ingrese el valor del ancho: ") 
        height = input("Ingrese el valor del alto: ")
        return Rectangule(float(width), float(height))
    
    @classmethod
    def __square_creation(cls):
        width = input("Ingrese el valor del ancho: ") 
        return Square(float(width))
    
    @classmethod
    def __circule_creation(cls):
        radius = input("Ingrese el valor del radio: ") 
        return Circule(float(radius))

    def create_shape(self,name_shape: str):
        types_shape = {
            "RECTANGULE": self.__rectangule_creation,
            "SQUARE": self.__square_creation,
            "CIRCULE": self.__circule_creation,
        }
        try:
            return types_shape[name_shape.upper()]()
        except Exception as e:
            print(f"The {name_shape} is not valid. {e}")
            raise e
        
        
def shapes_client():
    shape_factory = ShapeFactory()
    shape_name = input("Ingrese el nombre de la figura: ")
    shape = shape_factory.create_shape(shape_name)
    print(f"{type(shape)}")
    print(f"El area del {shape_name} es: {shape.calcule_area()}")
    print(f"El perimetro del {shape_name} es: {shape.calcule_perimeter()}")
    
if __name__ == '__main__':
    shapes_client()