class Carro():
    def arrancar(self):
        print(f"arrancar con carro marca: {self.marca}, color: {self.color}")

    #constructor
    def __init__(self, marca, modelo, color, puertas, combustible):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.puertas = puertas
        self.combustible = combustible

carro_uno = Carro("Mazda","XXRR","Blanco", 4, "gasolina")
print(carro_uno.puertas)
print(carro_uno.color)
carro_uno.arrancar()

carro_dos = Carro("Ford","F-150","Rojo","6", "gasolina")
print(carro_dos.modelo)
print(carro_dos.puertas)
print(carro_dos.color)
carro_dos.arrancar()

print(carro_uno.puertas)
print(carro_uno.color)
carro_uno.arrancar()