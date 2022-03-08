''' Generadores '''
# Los generadores en python son una funcion especial que permiten regresar una secuancia de valores pero no todos al mismo tiempo con la palabra reservada yield, suspendiendo la ejecucion de la funcion hasta que se llame a la funcion next(), por lo que no se usa la palabra return.

from typing import Generator

def generador():
    ''' Generador de numeros '''
    for i in range(10):
        yield i
      
# consumir el generador a demanda        
resultado = generador()
# con cada llamada se consume un valor
print(next(resultado))
print(next(resultado))
print(next(resultado))
print(next(resultado))
print(next(resultado))

print(''.center(20, '-'))

def generador2():
    ''' Generador de numeros '''
    for i in range(10):
        yield i

for item in generador2():
    print(item)
    
    
# generador de numeros del 1 al 5
def generador_numeros():
    for numero in range(1,6):
        yield numero
        print(f'Generando numero: {numero}')
        
for item in generador_numeros():
    print(item)
    
resultado2 = generador_numeros()
try:   
    print(next(resultado2))
    print(next(resultado2))
    print(next(resultado2))
    print(next(resultado2))
    print(next(resultado2))
    print(next(resultado2))
    print(next(resultado2))
    print(next(resultado2))
    print(next(resultado2))
    print(next(resultado2))
except StopIteration:
    print('Se termino el generador')
    
print(''.center(20, '-'))

# usando ciclo while

resultado3 = generador_numeros()
while True:
    try:
        valor = next(resultado3)
        print(valor)
    except StopIteration:
        print('Se termino el generador')
        break


# usando ciclo while en generador con funcion

def list_pares(limite: int)-> Generator[int, None, None]:
    num: int = 1
    
    while (num < limite):
        yield (num*2)
        num += 1

resultado_pares = list_pares(10)

print(resultado_pares)
print(type(resultado_pares))
for i in resultado_pares:
    print(i)