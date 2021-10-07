# trabajando con with y class para menejo de archivos

from ManejoArchivos import ManejoArchivos

with ManejoArchivos('archivos_copia.txt') as archivo:
    print(archivo.read())