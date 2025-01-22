numero = 5
texto = "Mensaje nuevo"

print(f"El valor del numero en la variable es {numero}, mientras que el valor del texo es: {texto}")

numero2 = 34

print(f"La suma de dos variables es: {numero + numero2}")

# Listas

lista = ["Python", "Angular", "Vue", "Nest", "Node"]

lista.append("Django")
lista.insert(4, "Express")

print(lista);

# tuplas: son inmutables. Las tuplas cuando tienen un dato deben terminar con la coma y el espacio
tupla1 = ("Python", "Angular", "Vue", "Nest", "Node")
print(tupla1[1]);

# diccionarios
datos = {
    "name": "Rocio",
    "lastname": "Sanchez",
    "age": "22",
    "country": "Spain",
    "language": "Python"
};

# agregar un dato
datos["city"] = "Barcelona"
# borrar un dato
del datos["country"]
# cantidad de claves
print(len(datos))

print(datos)
print(datos["name"])
