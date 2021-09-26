from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # en las clases heredadas se puede llamar a los metodos de la clase padre de manera individual
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return "El área del cuadrado es: {}".format(self.alto * self.ancho)

    def __str__(self):
        return f"{FiguraGeometrica.__str__(self)}. {Color.__str__(self)}"