class CuboHexaedro:
    """
        Calculo de la superficie de un cubo hexaedro regular
    """
    def __init__(self, lado):
        self.lado = lado
    def volumen(self):
        return self.lado ** 3

cubo1 = CuboHexaedro(6)
print(cubo1.volumen())

class CuboRectangular:
    """
        El volumen de un prisma rectangular se calcula como el producto de sus dimensiones (las aristas a, b y h). Un prisma rectangular (u ortoedro) es un poliedro cuya superficie está formada por dos rectángulos iguales y paralelos llamados bases y por cuatro caras laterales que son también rectángulos paralelos e iguales dos a dos. 
    """
    def __init__(self, alto, ancho, largo):
        self.lado = alto
        self.ancho = ancho
        self.largo = largo
    def volumen(self):
        return self.lado * self.ancho * self.largo

try:
    alto = float(input("Ingrese el alto del cubo: "))
    ancho = float(input("Ingrese el ancho del cubo: "))
    largo = float(input("Ingrese el largo del cubo: "))
    cubo2 = CuboRectangular(alto, ancho, largo)
    print(f"El volumen del Cubo Rectangular o Prisma Rectangular es: {cubo2.volumen():.2f} m3")
except ValueError:
    print("Error, los valores ingresados no son correctos")

