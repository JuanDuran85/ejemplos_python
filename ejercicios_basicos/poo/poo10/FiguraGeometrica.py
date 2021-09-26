# trabajando con clases abstractas ABC = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        if self.__validacion_valor(ancho):
            self.__ancho = ancho
        else:
            self.__ancho = 0
        if 0 < alto <= 20:
            self.__alto = alto
        else:
            self.__alto = 0
    
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if 0 < ancho <= 20:
            self.__ancho = ancho
        else:
            self.__ancho = 0
    @property
    def alto(self):
        return self.__alto

    @alto.setter
    def alto(self, alto):
        if self.__validacion_valor(alto):
            self.__alto = alto
        else:
            self.__alto = 0
    
    @abstractmethod
    def area(self):
        pass
    
    def __str__(self):
        return "Ancho: {}, Alto: {}".format(self.__ancho, self.__alto)

    def __validacion_valor(self, valor):
        return True if 0 < valor <= 20 else False
