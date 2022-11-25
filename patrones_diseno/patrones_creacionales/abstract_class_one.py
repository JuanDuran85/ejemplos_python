"""sumary_line

    Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared, but contains no implementation. Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.

    Python on its own doesn't provide abstract classes. Yet, Python comes with a module which provides the infrastructure for defining Abstract Base Classes (ABCs)

"""
from abc import ABC, abstractmethod

'''When defining an abstract class we need to inherit from the Abstract Base Class - ABC.

To define an abstract method in the abstract class, we have to use a decorator: @abstractmethod. The built-in abc module contains both of these.

If you inherit from the Animal class but don't implement the abstract methods, you'll get an error'''

class Animal(ABC):

    @abstractmethod
    def feed(self):
        pass

class Lion(Animal):
    def feed(self):
        return "feed the lion"

class Panda(Animal):
    def feed(self):
        return "feed the Panda"

class Snake(Animal):
    def feed(self):
        return "feed the Snake"

# creating and feeding animals
zoo = [Lion(), Panda(), Snake(),]
for animal in zoo:
    print(animal.feed())