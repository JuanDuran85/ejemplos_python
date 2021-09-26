from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # en las clases heredadas se puede llamar a los metodos de la clase padre de manera individual
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def area(self):
        return self.alto * self.ancho

    def __str__(self):
        return "Cuadrado de lado {} de color {}, tiene un área de: {}".format(self.alto, self.color, self.area())