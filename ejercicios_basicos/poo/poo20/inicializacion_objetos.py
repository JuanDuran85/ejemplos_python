# como se inicalizan los objetos en python

class Padre:
    def __init__(self):
        print("Inicializando padre")
        
    def metodos(self):
        print("Metodo padre")


class Hijo1(Padre):
    # si la clase hija tiene el metodo init se llama por defecto
    def __init__(self):
        # de manera opcional podemos llamar al metodo init de la clase padre
        super().__init__()
        print("Inicializando hijo")
        
    def metodos(self):
        print("Metodo padre sobreescrito en el hijo1")
        super().__init__()
        
class Hijo2(Padre):
    # si la clase hija no tiene metodo init se llama el metodo init del padre
    pass

hijo1 = Hijo1()
hijo1.metodos()
hijo2 = Hijo2()

# al instaciar el objeto automaticamente se ejecuta el metodo __init__
padre1 = Padre()
# llamando al metodo
padre1.metodos()

