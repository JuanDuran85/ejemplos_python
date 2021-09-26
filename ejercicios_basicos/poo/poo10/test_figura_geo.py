from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

cuadrado1 = Cuadrado(10, 'azul')
print(cuadrado1)
print(cuadrado1.color)
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.area())

# trabajando con el metodo MRO - Method Resolution Order
print(Cuadrado.__mro__)
print(Cuadrado.mro())

reactangulo1 = Rectangulo(10, 20, 'verde')
print(reactangulo1)
print(reactangulo1.color)
print(reactangulo1.ancho)
print(reactangulo1.alto)
print(reactangulo1.area())