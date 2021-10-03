class Monitor:
    contador_monitores = 0

    @classmethod
    def contar_monitores(cls):
        cls.contador_monitores += 1
        return cls.contador_monitores

    def __init__(self, marca, pulgadas):
        self.__id_monitores = Monitor.contar_monitores()
        self.__marca = marca
        self.__pulgadas = pulgadas

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def pulgadas(self):
        return self.__pulgadas

    @pulgadas.setter
    def pulgadas(self, pulgadas):
        self.__pulgadas = pulgadas

    @property
    def id_monitores(self):
        return self.__id_monitores

    def __str__(self):
        return "Id: {}. Monitor: {}, de {} pulgadas".format(self.id_monitores, self.marca, self.pulgadas)

if __name__ == "__main__":
    monitor1 = Monitor("HP", 22)
    monitor2 = Monitor("LG", 21)
    print(monitor1)
    print(monitor2)