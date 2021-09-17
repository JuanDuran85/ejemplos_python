'''
Realizar dos funciones para convertir de grados celsius a fahrenheit y viceversa.

Función 1. Recibir un parámetro llamado celcius y regresar el valor equivalente a fahrenheit

    La función se llama: celsius_fahrenheit(celsius) 

    La fórmula para convertir de celsius a fahrenheit es: celsius * 9/5 + 32  

Función 2. Recibir un parámetro llamado fahrenheit y regresar el valor equivalente a celsius:

    fahrenheit_celsius(fahrenheit)         

    La fórmula para convertir de fahrenheit a celsius es:  (fahrenheit-32) * 5/9

Los valores los debe proporcionar el usuario, utilizando la función input y convirtiendolo a tipo float.
'''

def celsius_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit-32) * 5/9
    return celsius

try:
    valor = float(input("Ingrese el valor a convertir: "))
    grados = input("Ingrese la escala a convertir: ")

    funcion_grados = {
    "F": celsius_fahrenheit,
    "C": fahrenheit_celsius,
    }

    if grados.upper() in funcion_grados:
        print(f"{valor} grados son {funcion_grados[grados.upper()](valor)} grados")
    else:
        print("No se puede convertir")
except:
    print("La escala ingresada no es válida")


# otra opción

def celsius_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

def fahrenheit_celsius(fahrenheit):
    celsius = (fahrenheit-32) * (5/9)
    return celsius

try:
    funcion_conver = {
        "F": celsius_fahrenheit,
        "C": fahrenheit_celsius,
    }

    unidades = {
        "F": 'Fahrenheit',
        "C": 'Celsius',
    }

    valor = float(input("Ingrese el valor a convertir: "))
    grados = input("Ingrese la escala a convertir: ")

    if funcion_conver[grados.upper()]:
        print(f"{valor} grados {'Celsius' if grados.upper() == 'F' else 'Fahrenheit'} son {funcion_conver[grados.upper()](valor)} grados {unidades[grados.upper()]}")
    else:
        print("La escala ingresada no es válida")

except ValueError:
    print("Valor ingresado no permitido")
except KeyError:
    print("No se permiten esos tipos de caracteres")
except:
    print("Ocurrió un error al ejecutar el programa")