from Producto import Producto

class Orden:

    contador_ordenes = 0

    @classmethod
    def contar_ordenes(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, productos):
        self.__id_orden = Orden.contar_ordenes()
        # no se debe asignar directamente, sino que se debe usar el metodo list
        self.__productos = list(productos)

    @property
    def id_orden(self):
        return self.__id_orden
    
    @property
    def productos(self):
        return self.__productos

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def total_orden(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        contador = 0
        for producto in self.productos:
            contador+=1
            productos_str += str(contador) + '. ' + (producto.__str__()) + '\n'
        return f'Orden {self.id_orden}. \nProductos: \n{productos_str}'

if __name__ == '__main__':
    producto1 = Producto("Papas", 1.5)
    producto2 = Producto("Manzanas", 2.5)
    producto3 = Producto("Peras", 3.5)
    producto4 = Producto("Cebollas", 4.5)
    producto5 = Producto("Tomates", 5.5)
    producto6 = Producto("Pimientos", 6.5)
    producto7 = Producto("Aceitunas", 7.5)
    producto8 = Producto("Pollo", 8.5)
    producto9 = Producto("Carne", 9.5)
    producto10 = Producto("Queso", 10.5)
    producto11 = Producto("Lechuga", 11.5)
    productos = [producto1, producto2, producto3, producto4, producto5, producto6, producto7, producto8, producto9, producto10, producto11]
    orden = Orden(productos)
    print(orden)