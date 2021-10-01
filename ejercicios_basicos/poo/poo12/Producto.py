class Producto:
    contador_producto = 0

    @classmethod
    def aumenta_contador(cls):
        cls.contador_producto += 1
        return cls.contador_producto

    def __init__(self, nombre, precio):
        self.__id_producto = Producto.aumenta_contador()
        self.__nombre = nombre
        self.__precio = precio

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return "Id producto: {}. Nombre: {}. Precio: {}".format(self.__id_producto, self.nombre, self.precio)

if __name__ == "__main__":
    producto1 = Producto("Papas", 1.5)
    producto2 = Producto("Manzanas", 2.5)
    print(producto1)
    print(producto2)
