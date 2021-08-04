from fichero_export import CarroDeportivo, Carro

carro1 = Carro("Mazda", "MX-5", "Rojo", 4)
carro_deport = CarroDeportivo("Ferrari", "F50", "Azul", 2, 200)
carro1.estado()
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

print("--------------------------")
carro_deport.estado()
print(f"Caballos de Fuerza: {carro_deport.caballos}")
print("--------------------------")