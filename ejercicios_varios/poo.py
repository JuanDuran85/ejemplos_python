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

carro1 = Carro("Mazda", "MX-5", "Rojo", 4)
carro2 = Carro("Ferrari", "F50", "Azul", 2)
carro1.estado()
carro2.estado()
carro1.arrancar()
carro1.acelerar()
carro1.acelerar()
if carro1.encendido:
    print(f"El carro está encendido y la velocidad es: {carro1.velocidad}")
    carro1.frenar(20)
    print(f'La valocidad actual es: {carro1.velocidad}')
    print(f'El año del carro es: {carro1.get_year()}')
    print()
else:
    print("El carro está apagado")