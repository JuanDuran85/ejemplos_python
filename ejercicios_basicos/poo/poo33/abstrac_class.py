"""_summary_

    Working with abstract class and ABC library
    
    Los metodos abstractos se deben declarar en las clases que heradan la clase abstracta

"""

from abc import abstractmethod, ABCMeta

class ClaseBaseAbstracta(metaclass=ABCMeta):
    
    @abstractmethod
    def metodo_uno(self) -> str: ...

    @abstractmethod
    def metodo_dos(self) -> str: ...
    
class ClaseConcreta(ClaseBaseAbstracta):
    
    def metodo_uno(self) -> str:
        return "Metodo uno implementado"
    
    def metodo_dos(self)-> str: 
        return "Metodo dos implementado"
    
ejemplo_uno: ClaseConcreta = ClaseConcreta()
print(ejemplo_uno.metodo_uno())
print(ejemplo_uno.metodo_dos())