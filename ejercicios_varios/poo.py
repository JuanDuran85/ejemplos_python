class Carro():
    marca = ""
    modelo = ""
    color = ""
    numero_puertas = 0

    def __init__(self, marca, modelo, color, numero_puertas):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.numero_puertas = numero_puertas

carro1 = Carro("Mazda", "MX-5", "Rojo", 4)
carro2 = Carro("Ferrari", "F50", "Azul", 2)

print(f'Marca: {carro1.marca}. Color: {carro1.color}. Modelo: {carro1.modelo}. Numero de puertas: {carro1.numero_puertas}')
print(f'Marca: {carro2.marca}. Color: {carro2.color}. Modelo: {carro2.modelo}. Numero de puertas: {carro2.numero_puertas}')