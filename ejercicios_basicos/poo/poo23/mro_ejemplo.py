''' Entendiendo MRO - Method Resolution Order para herencia multiple'''

class Clase1:
    """Clase 1 - Clase padre"""
    def __init__(self):
        print("Clase1.__init__")
    
    def metodo(self):
        print("Clase1.metodo")
        
class Clase2(Clase1):
    """Clase 2 - Clase hija"""
    def __init__(self):
        print("Clase2.__init__")
        super().__init__()
        
    def metodo(self):
        print("Clase2.metodo")
        super().metodo()
        
class Clase3(Clase1):
    """Clase 3 - Clase hija"""
    def __init__(self):
        print("Clase3.__init__")
        super().__init__()
        
    def metodo(self):
        print("Clase3.metodo")
        super().metodo()

# aplicando herencia multiple
# la primera clase que se herada es la mas importante

class Clase4(Clase2,Clase3):
    def metodo(self):
        print("Clase4.metodo")
        super().metodo()

# creando objeto para la clase4 para poner en practica MRO - Method Resolution Order
clase4 = Clase4()
# para saber cuales son las clases padre de la clase4, se usa el atributo __bases__
print(Clase4.__bases__)
# para saber hasta la ultima clase padre
print(Clase4.__mro__)
# cual metodo se ejecuta primero
clase4.metodo()