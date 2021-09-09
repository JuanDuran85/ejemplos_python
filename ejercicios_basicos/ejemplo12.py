# Trabajando con Listas

nombres = ["Juan", "Pedro", "Ana", "Maria", "Luis", "Carlos"]

# para acceder a un elemento de la lista se puede usar el indice negativo, lo que nos devolvera el elemento desde el final al incio
print(nombres[-1])
print(nombres[-4])
print(nombres[1])
print(nombres[4])

# desde un indicador de inicio hasta un indicador de fin
print(nombres[1:4])
print(nombres[:4])
print(nombres[4:])

# recorriendo una lista
for nombre in nombres:
    print(nombre)

# ver el largo de una lista
print(len(nombres))

# agregar un nuevo elemento a una lista
nombres.append("Jorge")
print(nombres)

# insertar un elemento en una posicion determinada
nombres.insert(2, "Elio")
print(nombres)

# remover un elemento de una lista
nombres.remove("Ana")
print(nombres)

# remover el ultimo elemento de una lista
nombres.pop()
print(nombres)

# remover un elemento en una posicion determinada
nombres.pop(2)
print(nombres)

# eliminar un indice de una lista
del nombres[2]
print(nombres)

# copiar una lista
copia = nombres.copy()
print(f"la copia es: {copia}")

# limpiar una lista
nombres.clear()
print(nombres)

# borrar la lista
del nombres

try:
    if nombres:
        print(nombres)
except NameError as error:
    print(f"El error es: {error}")