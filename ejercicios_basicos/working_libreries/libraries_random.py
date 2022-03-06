"""_summary_

 Trabajando con la libreria Random

"""

import random

#-------------------------------------------------------------------------------------
def cargar() -> list:
    lista: list = []
    for _ in range(10):
        lista.append(random.randint(1, 100))
    return lista

def imprimir(lista: list) -> None:
    print(lista)
    
def mezcla(lista: list) -> list:
    random.shuffle(lista)        
    
if __name__ == '__main__':
    lista = cargar()
    print("Lista creada...")
    imprimir(lista)
    mezcla(lista)
    print("Lista mezclada...")
    imprimir(lista)
#-------------------------------------------------------------------------------------