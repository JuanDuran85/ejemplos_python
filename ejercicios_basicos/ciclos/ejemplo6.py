datos = [32, 4, 5, 6, 7, 67]
datos.append(-23)
datos.append(8)
print("Datos 3,5")
print(datos[3])
print(datos[5])

print("Todos los datos del arreglo estatico")
for x in range(0, 6):
    print(datos[x])

print("Todos los datos del arreglo inversamente")
for x in range(5, -1, -1):
    print(datos[x])

print("Todos los datos del arreglo dinamico")
for x in range(0, len(datos)):
    print(datos[x])

print("-------------------")

valores = []
for i in range(0, 6):
    valores.append(int(input("Ingresa un valor: ")))

valores[2] = -5

for i in range(5, -1, -1):
    print(valores[i])
