class Dispositivo_Entrada:
    def __init__(self, tipo_entrada, marca):
        self.__tipo_entrada = tipo_entrada
        self.__marca = marca

    @property
    def tipo_entrada(self):
        return self.__tipo_entrada

    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        self.__tipo_entrada = tipo_entrada

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    def __str__(self):
        return f"Dispositivo de entrada: {self.__tipo_entrada} de marca {self.__marca}"