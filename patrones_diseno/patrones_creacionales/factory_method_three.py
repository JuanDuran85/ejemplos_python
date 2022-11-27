"""
El patrón Factory Method sugiere que, en lugar de llamar al operador new para construir objetos directamente, se invoque a un método fábrica especial. Los objetos devueltos por el método
fábrica a menudo se denominan productos.

Limitación: las subclases sólo pueden devolver productos de distintos tipos si dichos productos tienen una clase base o interfaz común. Además, el método fábrica en la clase base debe tener su tipo de retorno declarado como dicha interfaz. 

"""

# first part - We start by creating the Object Interface, with the common attributes and functionality among the various X classes  written and stored in the x class. For example, Burger class.

# patent class - Object  Interface
from typing import Type


class Burger(object):
    def cook(self): ...

# children class
class BeefBurgers(Burger):
    def cook(self)-> None:
        print("Cooking Beef Burgers")

class ChikenBurgers(Burger):
    def cook(self)-> None:
        print("Cooking Chiken Burgers")

class FishBurgers(Burger):
    def cook(self)-> None:
        print("Cooking Fish Burgers")
        
        
# Next the Factory Object is created. The library's Factory will accept an input and decide which object type to create.
class BurgerStoreFactory(object):
    @staticmethod
    def get_burger(name: str)-> (BeefBurgers | ChikenBurgers | FishBurgers):
        types_burger:  dict[str, Type[BeefBurgers] | Type[ChikenBurgers] | Type[FishBurgers]] = {
            'BEEF': BeefBurgers,
            'CHIKEN': ChikenBurgers,
            'FISH': FishBurgers
        }
        try:
            return types_burger[name.upper()]()
        except KeyError as e:
            print(f"The value: {name} is not valid")
            raise e
        
# clien code
if __name__ == '__main__':

    creating_burger: BurgerStoreFactory = BurgerStoreFactory()
    beef_burger = creating_burger.get_burger('beeeef')
    beef_burger.cook()

