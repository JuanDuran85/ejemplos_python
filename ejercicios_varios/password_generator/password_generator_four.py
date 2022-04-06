"""_summary_

    Generador basico de contraseñas

"""

import random

letras: list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numeros: list = [0,1,2,3,4,5,6,7,8,9]
simbolos: list = ['|','!','<','>','#','$','%','&','*','(',')','-','_','=','+','^','*','(',')','[',']','{','}','\\',';',':',',','.','/','?']

print("Generador de contraseñas")

lista_result: list = []

def valores_random(elemento: str, cantidad: int) -> None:
    for _ in range(1, cantidad + 1):
        valor: str = random.choice(elemento)
        lista_result.append(valor)

try:
    numero_letras: int = int(input("Introduce el numero de letras que quieres que tenga la contraseña: "))
    numero_numeros: int = int(input("Introduce el numero de numeros que quieres que tenga la contraseña: "))
    numero_simbolos: int = int(input("Introduce el numero de simbolos que quieres que tenga la contraseña: "))
    
    valores_random(letras, numero_letras)
    valores_random(numeros, numero_numeros)
    valores_random(simbolos, numero_simbolos)
    random.shuffle(lista_result)
    print("".join(map(str,lista_result)))
    
except Exception as e:
    print("Error: ", e)
    raise e