import os, sys
from os.path import join, isfile
from os import listdir

simbolos: dict = {
    "clubs": "treboles",
    "diamonds": "diamantes",
    "hearts": "corazones",
    "spades": "espadas"
}

numeros: dict = {
    "king":"K",
    "queen":"Q",
    "jack":"J",
    "ace":"A"
}

def renombrar_archivo(archivos: list):
    for archivo in archivos:
        partes: list = archivo.split("_")
        if len(partes) == 3 and partes[2][0:-4] in simbolos:
            print(partes)
            num: str = partes[0]
            if num in numeros:
                num = numeros[partes[0]]
                
            nuevo_nombre: str = f"{num}_de_{simbolos[partes[2][0:-4]]}.png"
            print(nuevo_nombre)
            os.rename(f"{ruta}/{archivo}", f"{ruta}/{nuevo_nombre}")

try:
    ruta: str = sys.argv[1]
    solo_archivos: list = [file for file in listdir(ruta) if isfile(join(ruta, file))]
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
    
if __name__ == '__main__':
    renombrar_archivo(solo_archivos)