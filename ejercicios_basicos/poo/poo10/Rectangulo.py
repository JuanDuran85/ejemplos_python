from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, base, altura, color):
        FiguraGeometrica.__init__(self, base, altura)
        Color.__init__(self, color)

    def area(self):
        return self.ancho * self.alto

    def __str__(self):
        return "Rectangulo de base {}, altura {} y color {}, con un area de: {}".format(self.ancho, self.alto, self.color, self.area())