"""_summary_

    Working with library PDB
    Depuracion de codigo
    comandos de la libreria:
    - list: para mostrar todo el programa
    - step: para entrar dentro de un proceso y seguir con la ejecucion paso a paso
    - next: para continuar con la siguiente linea de ejecucion
    - continue: para continuar con el programa hasta el final
    - list x,y: x e y permiten indicar cuales lineas queremos mostrar del programa
    - break x: para agregar un nuevo punto de quiebre en la linea en especifico
    - jumb x: para saltar a la linea en especifico
    - pp x: para visualizar el valor de la varibale indicada
    - disable: permite desactivar los puntos de quiebre
    - exit(): podemos salir del programa forzadamente  

"""

import pdb

# Tabla de multiplicar
# Tabla del 2

print("Inicio de la ejecucion del programa")

pdb.set_trace()

base: int = 2
for i in range(1,11):
    mutiplicacion: int = i * base
    print(f"{i} x {base} = {mutiplicacion}")
    
print("Fin de la ejecucion del programa")