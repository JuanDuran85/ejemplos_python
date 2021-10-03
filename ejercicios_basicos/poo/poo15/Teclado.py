from DispositivoEntrada import Dispositivo_Entrada

class Teclado(Dispositivo_Entrada):

    contador_teclado = 0

    @classmethod
    def contar(cls):
        cls.contador_teclado += 1
        return cls.contador_teclado

    def __init__(self, marca, tipo_entrada):
        self.__id_teclado = Teclado.contar()
        super().__init__(marca, tipo_entrada)

    @property
    def id_teclado(self):
        return self.__id_teclado

    def __str__(self):
        return "Id: {}. Marca: {}. Tipo de entrada: {}".format(self.id_teclado, self.marca, self.tipo_entrada)

if __name__ == "__main__":
    teclado1 = Teclado("USB", "Logitech")
    teclado2 = Teclado("USB", "HP")
    print(teclado1)
    print(teclado2)
