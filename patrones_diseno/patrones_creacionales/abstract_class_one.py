"""sumary_line

    Abstract classes are classes that contain one or more abstract methods. An abstract method is a method that is declared, but contains no implementation. Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.

    Python on its own doesn't provide abstract classes. Yet, Python comes with a module which provides the infrastructure for defining Abstract Base Classes (ABCs)

"""
from abc import ABC, abstractmethod

'''When defining an abstract class we need to inherit from the Abstract Base Class - ABC.

To define an abstract method in the abstract class, we have to use a decorator: @abstractmethod. The built-in abc module contains both of these.

If you inherit from the Animal class but don't implement the abstract methods, you'll get an error'''

class Animal(ABC):

    @property
    def food_eaten(self):
        return self._food

    @food_eaten.setter
    def food_eaten(self, food):
        if food in self.diet:
            self._food = food
        else:
            raise ValueError(f"you can't feed this animal with {food}")
    
    @property
    @abstractmethod
    def diet(self): ...
    
    @abstractmethod
    def feed(self): ...

    def do_action(self, action): ...

class Lion(Animal):
    @property
    def diet(self):
        return ["antelope","sheep","buffaloe"]

    def feed(self, time="1300"):
        return f"feeding the lion with {self._food} at {time}"

    def do_action(self, action, extra_time="900"):
        return f"{action} a Lion, at {extra_time}"

class Panda(Animal):
    @property
    def diet(self):
        return ["bambu"]

    def feed(self, time="1300"):
        return f"feeding the panda with {self._food} at {time}"

    def do_action(self, action, extra_time="900"):
        return f"{action} a Panda, at {extra_time}"

class Snake(Animal):
    @property
    def diet(self):
        return ["frog","rabbit","mouse"]

    def feed(self, time="1300"):
        return f"feeding the snake with {self._food} at {time}"

    def do_action(self, action, extra_time="900"):
        return f"{action} a Snake, at {extra_time}"

# creating and feeding animals
zoo = [Lion(), Panda(), Snake(),]
food = ["antelope","bambu","frog"]
for animal,meal in zip(zoo,food):
    animal.food_eaten = meal 
    print(animal.feed())
    print(animal.do_action(action="feeding",extra_time="9:00"))

# creating and feeding animals with property, setter and abstract methods
lion = Lion()
lion.food_eaten = "buffaloe"
print(lion.feed(time="1850"))
