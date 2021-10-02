from Ordenes import Orden
from Producto import Producto

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
productos_uno = [producto1, producto2, producto3, producto4, producto5]
productos_dos = [producto6, producto7, producto8, producto9, producto10, producto11]
orden = Orden(productos_uno)
orden2 = Orden(productos_dos)
print(orden,end='')
print("Total Orden 1: {}".format(orden.total_orden()))
print("")
print(orden2,end='')
print("Total Orden 2: {}".format(orden2.total_orden()))