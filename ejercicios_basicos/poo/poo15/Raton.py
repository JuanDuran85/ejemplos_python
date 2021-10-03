from DispositivoEntrada import Dispositivo_Entrada

class Raton(Dispositivo_Entrada):

    contador_ratones = 0

    @classmethod
    def contador(cls):
        cls.contador_ratones += 1
        return cls.contador_ratones

    def __init__(self, marca, tipo_entrada):
        self.__id_ratones = Raton.contador()
        super().__init__(marca, tipo_entrada)

    @property
    def id_ratones(self):
        return self.__id_ratones

    def __str__(self):
        return "Id: {}. Marca: {}. Tipo de entrada: {}".format(self.id_ratones, self.marca, self.tipo_entrada)

if __name__ == "__main__":
    raton1 = Raton("USB", "Logitech")
    print(raton1)
    raton2 = Raton("Blue", "HP")
    print(raton2)