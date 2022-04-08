# las funciones en python son ciudadanos de primera clase (FCC)
# First Class Citizen

from typing import Any

def sumar(a, b):
    return a + b

# 1. Asignar una funcion a una variable

mi_funcion = sumar(5,8)
print(mi_funcion)

# 2. Funcion como argumento y retorno de una funcion dentro de otra

def operacion(a,b,sumar_argumento):
    return sumar_argumento(a,b)

print(f"Resultado: {operacion(3,4,sumar)}")

# 3. Retornar una funcion

def retorno_funcion():
    return sumar

mi_funcion_retornada = retorno_funcion()
print(f"Resultado: {mi_funcion_retornada(15,10)}")


# se puede usar *args para pasar una lista de argumentos indeterminados a una funcion
def varios_argumentos(*args: Any) -> None:
    total_elementos: int = len(args)
    for i,elmento in enumerate(args):
        print(f"Elemento {i+1} de {total_elementos}: {elmento}")
        
varios_argumentos(1,"Cadena de texto", [1,2,3,4], {"clave":"valor"})

# se puede usar **kewargs para pasar un diccionario de argumentos indeterminados a una funcion.Cnstruye un diccionario con los argumentos pasados
def argumentos(**kwargs) -> None:
    print(f"Diccionario de argumentos: {kwargs}")
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    
argumentos(clave1="valor1", clave2="valor2")

# Se pueden utilizar *args y **kwargs combinados como argumentos indeterminados de una funcion
def argumentos_indeterminados(*args, **kwargs) -> None:
    suma: int = 0
    for e in args:
        suma += e
    print(f"El promedio es: {(suma/len(args)).__round__(2)}")
    for clave in kwargs:
        print(clave, "\t", kwargs[clave])    
argumentos_indeterminados(10,20,30,10,10,20, id = 5, nombre= "Isabell", edad = 23, notas=[10,12,20,20,17])

'''
 Se desea hacer una función que ayude a determinar la cantidad de dígitos que posee un número. La función recibirá un número entero cualquiera y retornara la cantidad de dígitos que compone el número. Considere que la función puede recibir números enteros positivos o negativos
 Por ejemplo: 
 -- Si se recibe 124 el valor de retorno será 3
 -- Si se recibe 638290 el valor de retorno será 6
'''
def calcular_cantidad_digitos(numero: int) -> int:
    return len(str((numero*-1))) if numero <= -1 else len(str(numero))

print(calcular_cantidad_digitos(-3))