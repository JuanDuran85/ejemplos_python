"""_summary_

    Working with copy library

    El metodo copy sirve para hacer copias pocos profundas (shallow)
    El metodo deepcopy sirve para hacer copias profundas (deep)
    
"""

from copy import copy, deepcopy

# ------------------------------------------------------------------------------------------------
# utilizando el metodo deepcopy para generar copias profundas (deep) y evitar cambios por referncia de objetos
lista_a: list = [[1,2],[3,4],[5,6]]
list_b_copy: list = deepcopy(lista_a)
print(f"{lista_a = }")
print(f"{list_b_copy = }")

# si modificamos el primer objeto, estos cambios no se veran reflejados en el objeto copia
lista_a.append([7,8])
print(f"{lista_a = }")
print(f"{list_b_copy = }")

# Igualmente, si realizamos modificacion en los elementos internos del objeto padre, estos no se veran reflejados en el objeto copia
lista_a[0][1] = 'A'
print(f"{lista_a = }")
print(f"{list_b_copy = }")

# ------------------------------------------------------------------------------------------------
# Ejemplo con copias superficiales para instancias de clases

class Punto:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y
        
    def __repr__(self):
        return f"Punto({self.x!r}, {self.y!r})"
    
    def __eq__(self, in_obj: object) -> bool:
        return isinstance(in_obj, Punto) and self.x == in_obj.x and self.y == in_obj.y

punto_a: Punto = Punto(1,2)
# copia poco profunda con la libraria copy metodo copy
punto_b_copy: Punto = copy(punto_a)
print(f"{punto_a = }")
print(f"{punto_b_copy = }")
print(f"Tienen la misma referencia? {punto_a is punto_b_copy}")
print(f"Son objetos con el mismo contenido? {punto_a == punto_b_copy}")

# ------------------------------------------------------------------------------------------------
# Ejemplo con copias profundas y superficiales para instancias de clases

class Rectangulo:
    def __init__(self, punto_1: Punto, punto_2: Punto) -> None:
        self.punto_1 = punto_1
        self.punto_2 = punto_2

    def __repr__(self):
        return f"{self.__class__.__name__}({self.punto_1!r}, {self.punto_2!r})"
    
rectangulo_1: Rectangulo = Rectangulo(Punto(1,2), Punto(3,4))
# copia superficial
rectangulo_copy: Rectangulo = copy(rectangulo_1)
print(f"{rectangulo_1 = }")
print(f"{rectangulo_copy = }")

# como es copia superficial, al realizar un cambio en el objeto principal, se ve reflejado en al copia
rectangulo_1.punto_1.x = 5
print(f"{rectangulo_1 = }")
print(f"{rectangulo_copy = }")

# realizando una copia profunda
rectangulo_copy_2: Rectangulo = deepcopy(rectangulo_1)

# al modficiar un valor en cualquiera de los objetos, estos no sufren alteraciones en la copia
rectangulo_copy_2.punto_1.x = -6
rectangulo_1.punto_2.y = -7
print(f"{rectangulo_1 = }")
print(f"{rectangulo_copy_2 = }")
