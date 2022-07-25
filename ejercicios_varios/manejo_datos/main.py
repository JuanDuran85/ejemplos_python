import os
import sys
import time

import preguntas as p
from level import choose_level
from print_preguntas import print_pregunta
from question import choose_q
from validador import validate
from verify import verificar

n_pregunta: int = 0
continuar: str = 'y'
correcto: bool = True
p_level: int = 10
op_sys: str = 'cls' if sys.platform == 'win32' else 'clear'
os.system(op_sys)

print('Bienvenido a la Trivia')
opcion = input('''Ingrese una opción para Jugar!
        1. Jugar
        0. Salir
        
    > ''')
opcion = validate(['1', '0'], opcion)

# 2. Definir el comportamiento de Salir
if opcion == '0':
    print("Saliendo...")
    time.sleep(2)
    os.system(op_sys)
    sys.exit()
    
while correcto and n_pregunta < 3*p_level:
    
    if n_pregunta == 0:
        p_level = input('¿Cuántas preguntas por nivel? (Máximo 3): ')
        p_level = int(validate(['1','2','3'], p_level))
        
    if continuar == 'y':
        n_pregunta += 1
        nivel = choose_level(n_pregunta, p_level)
        print(f'Pregunta {n_pregunta}:')
        enunciado, alternativas = choose_q(nivel)
        print_pregunta(enunciado, alternativas)
        respuesta: str = input('Escoja la alternativa correcta:\n> ').lower()

        respuesta = validate(['a','b','c','d'],respuesta)
        correcto = verificar(alternativas, respuesta)
        
        if correcto and n_pregunta < 3*p_level:
            print('Muy bien sigue así!')
            continuar = input('Desea continuar? [y/n]: ').lower()
            continuar = validate(['y','n'],continuar)
            os.system(op_sys)
        elif correcto and n_pregunta == 3*p_level:
            print(f'Felicitaciones, Has respondido {3*p_level} preguntas correctas. \n Has ganado la Trivia \n Gracias por Jugar, hasta luego!!!')
            time.sleep(3)
            os.system(op_sys)
        else: 
            print(f'Lo siento, conseguiste {n_pregunta - 1} respuestas correctas,\n Sigue participando!!')
            time.sleep(3)
            exit()
    else: 
        print('Nos vemos la proxima vez, sigue practicando')
        time.sleep(3)
        exit()
            
            
