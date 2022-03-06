# cargar archivo
from io import TextIOWrapper

archivo: TextIOWrapper = open("archivo.txt", "w+")

# se solicita la escritura al usuario
a_escribir: str = input("Ingresa el texto a escribir: ")

# leer archivo
contenido: str = archivo.read()
# calcular el final del archivo, retornando la posicion actual del puntero
final_del_archivo: int =  archivo.tell()

# escribimos en el archivo
archivo.writelines(a_escribir)

# otro mensaje a escribir en el archivo
lista: list = ['Linea 1\n', 'Linea 2\n', 'Linea 3\n']
archivo.writelines(lista)

# mover elpuntero al byte indicado
archivo.seek(final_del_archivo)

# almacenar todo el contenido en la varibale al leerlo
nuevo_contenido: str = archivo.read()

# se cierra el procedimiento
archivo.close()

print(nuevo_contenido)