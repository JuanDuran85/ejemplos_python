from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado

class Computadora:

    contador_computadora = 0

    @classmethod
    def contar_computadoras(cls):
        cls.contador_computadora += 1
        return cls.contador_computadora

    def __init__(self, nombre, monitor, teclado, raton):
        self.__id_computador = Computadora.contar_computadoras()
        self.__nombre = nombre
        self.__monitor = list(monitor)
        self.__teclado = list(teclado)
        self.__raton = list(raton)

    @property
    def id_computador(self):
        return self.__id_computador

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def monitor(self):
        return self.__monitor

    @monitor.setter
    def monitor(self, monitor):
        self.__monitor = monitor
    
    @property
    def teclado(self):
        return self.__teclado

    @teclado.setter
    def teclado(self, teclado):
        self.__teclado = teclado

    @property
    def raton(self):
        return self.__raton

    @raton.setter
    def raton(self, raton):
        self.__raton = raton

    def detalles(self,objeto):
        producto_str = ''
        for producto in objeto:
            producto_str += str(producto.__str__()) + '\n'
        return producto_str

    def __str__(self):
        return "{}. Computadora: {}\nMonitor: \n{}\nTeclado: \n{}\nRaton: \n{}".format(self.id_computador, self.__nombre, self.detalles(self.monitor), self.detalles(self.teclado), self.detalles(self.raton))

if __name__ == "__main__":
    monitor1 = Monitor("HP", 22)
    monitor2 = Monitor("LG", 24)
    teclado1 = Teclado("HP", "USB")
    teclado2 = Teclado("Dell", "USB")
    raton1 = Raton("HP", "USB")
    raton2 = Raton("Dell", "USB")
    monitores = [monitor1, monitor2]
    teclados = [teclado1, teclado2]
    ratones = [raton1, raton2]

    computadora_1 = Computadora("Computadora 1", monitores, teclados, ratones)
    print(computadora_1)
    computadora_2 = Computadora("Computadora 2", monitores, teclados, ratones)
    print(computadora_2)
