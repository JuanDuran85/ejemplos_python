class Carro():
    marca = ""
    modelo = ""
    color = ""
    numero_puertas = 0
    encendido = False
    velocidad = 0
    __year = 2020

    def estado(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Color: ", self.color)
        print("Numero de puertas: ", self.numero_puertas)
        print("Encendido: ", self.encendido)
        print("Velocidad: ", self.velocidad)
        print("Año: ", self.__year)

    def __init__(self, marca, modelo, color, numero_puertas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.numero_puertas = numero_puertas
    
    def arrancar(self):
        self.encendido = True
    
    def apagar(self):
        self.encendido = False
    
    def acelerar(self):
        self.velocidad += 35

    def frenar(self, valor):
        self.velocidad = valor

    def get_year(self):
        return self.__year

class CarroDeportivo(Carro):
    caballos = 150

    def __init__(self, marca, modelo, color, numero_puertas, caballos):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.numero_puertas = numero_puertas
        self.caballos = caballos