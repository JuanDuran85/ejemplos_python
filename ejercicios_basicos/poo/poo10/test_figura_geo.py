from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print("Creacion objeto Cuadrado".center(50, "-"))
cuadrado1 = Cuadrado(lado=10, color='azul')
print(cuadrado1)
print(cuadrado1.color)
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.area())

# trabajando con el metodo MRO - Method Resolution Order
print(Cuadrado.__mro__)
print(Cuadrado.mro())

print("Creacion Objeto Rectangulo".center(50, "-"))
reactangulo1 = Rectangulo(base=-10, altura=20,color='verde')
print(reactangulo1)
print(reactangulo1.color)
print(reactangulo1.ancho)
print(reactangulo1.alto)
print(reactangulo1.area())