"""
    Patron de diseño: Factory Method.
"""

# fabrica de objetos que seran figuras geometricas y cada uno de estos objetos tendra una operacion polimorfica que sera un metodo para calcular el area de cada uno de los objetos geometricos

from abc import ABC, abstractmethod
import math

# clase abstracta o interface
class IShape(ABC):
    
    @abstractmethod
    def area(self) -> int: ...    

# creando figuras geometricas 
class Triangulo(IShape):
    
    def __init__(self, width: int, heigth: int):
        self.width = width
        self.heigth = heigth
    
    def area(self) -> int:
        return (self.width * self.heigth) // 2
    
class Rectangulo(IShape):
    
    def __init__(self, width: int, heigth: int):
        self.width = width
        self.heigth = heigth
    
    def area(self) -> int:
        return self.width * self.heigth

class Circule(IShape):
    
    def __init__(self, radius: int):
        self.radius = radius
        
    def area(self) -> int:
        return (math.pi * (self.radius ** 2))

# creando la factoria
class IShapeFactory(ABC):
    @abstractmethod
    def get_shape(self) -> IShape: ...

# fabrica de rectangulos
class RectangleFactory(IShapeFactory):
    
    def get_shape(self, width: int, heigth: int) -> IShape:
        return Rectangulo(width=width, heigth=heigth)
    
# fabrica de triangulos
class TriangleFactory(IShapeFactory):
    
    def get_shape(self, width: int, heigth: int) -> IShape:
        return Triangulo(width=width, heigth=heigth)
    
# fabrica de circulos
class CirculeFactory(IShapeFactory):
    
    def get_shape(self, radius: int) -> IShape:
        return Circule(radius=radius)
    
# clase para metodo estatico de calculo de area
class AreaCalculator:
    @staticmethod
    def calc_area(shape: IShapeFactory, *args):
        """ calcular el arrea de una figura esoecifica"""        
        shape = shape.get_shape(*args)
        return shape.area()

# metodo para leer la factoria
def read_factory() -> IShapeFactory:
    factories = {
        'rec': RectangleFactory,
        'tria': TriangleFactory,
        'cir': CirculeFactory
    }
    
    while True:
        option = str(input("Ingrese la figura geometrica que desea calcular el area (rec: Rectangulo, tria: Triangulo, cir: Circulo): ")).lower()
        if option in factories:
            return factories[option]()
        else:
            print("Opcion invalida")

if __name__ == '__main__':
    factory_select = read_factory()
    area_factoy = AreaCalculator.calc_area(factory_select, 4)
    print(f"El area de la figura geometrica es: {area_factoy}")