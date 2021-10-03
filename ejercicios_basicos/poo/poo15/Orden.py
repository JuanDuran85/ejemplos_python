class Orden:

    contador_ordenes = 0

    @classmethod
    def contar_ordenes(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, computadoras):
        self.__id_orden = Orden.contar_ordenes()
        self.__computadoras = list(computadoras)

    @property
    def id_orden(self):
        return self.__id_orden

    @property
    def computadoras(self):
        return self.__computadoras

    def agregar_computadoras(self, computadora):
        self.__computadoras.append(computadora)

    def lista_computadores(self, computadores):
        computador_str = ""
        for computadora in computadores:
            computador_str += str(computadora) + "\n"
        return computador_str

    def __str__(self):
        return "Orden: " + str(self.id_orden) + "\n" + self.lista_computadores(self.computadoras)