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

# ----------------------------------------------------------------------------------------
# Programe una función que reciba una lista de números y retorne la multiplicación de cada una de sus celdas.

def multiplicar_celdas(lista: list) -> int:
    acumulado: int = 1 if len(lista)>=1 else 0
    for _,value in enumerate(lista):
        acumulado *= value
    return acumulado

print(multiplicar_celdas([1,2,3,4,5]))

# -------------------------------------------------------------------------------------------
# Se quiere implementar una función que sea capaz de recibir una lista de números enteros y nos retorne un número entero con la unión de cada una de sus celdas. Por ejemplo si se recibe la lista: [11,2,34,5] el valor de retorno será: 112345. El tamaño de la lista puede variar. Si recibe un número negativo, debe ignorar el signo tomar su parte positiva para procesarlo por ejemplo si se recibe la lista [1,-2,3,-4,-5] el valor de retorno será: 12345

def formar_numero(lista: list) -> int:
    numero_final: str = ""
    for _,value in enumerate(lista):
        if value <= -1:
            value *= -1
        numero_final += str(value)
        
    return int(numero_final) if len(lista) > 0 else 0

print(formar_numero([]))

# --------------------------------------------------------------------------------------
# imprimir matrices de una menor manera

print("\t\r\n")
def imprimir_matriz(matriz: list) -> None:
    contenido: str = ""
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            contenido += str(matriz[f][c]) + "\t"
        contenido += "\n"
    print(contenido)
    
matriz_uno: list = [None] * 3

for celda in range(len(matriz_uno)):
    matriz_uno[celda] = [1] * 3
    
imprimir_matriz(matriz_uno)

# ---------------------------------------------------------------------------------------------
# Su misión es crear una matriz que representa una tabla de multiplicar de tamaño NxN, donde N corresponde al valor que representa el tamaño recibido por parámetro. Para valores 0 o negativos, deberá devolver una matriz vacía.

def crear_tabla_multiplicar(n: int) -> list:
    if n <= -1:
        return []
    matriz_final: list = []
    lista_interna: list = []
    for i in range(n):
        for j in range(n):
            lista_interna.append((i+1)*(j+1))
        matriz_final.append(lista_interna)
        lista_interna = []
    return matriz_final
            
result: list = crear_tabla_multiplicar(-5)
imprimir_matriz(result)

# ---------------------------------------------------------------------------------------------
# Programe una función que determine si una palabra recibida por parámetro es un palíndromo o no. Un palíndromo es una palabra que se puede leer de la misma forma de izquierda a derecha o derecha a izquierda, por ejemplo: 'Ana', 'aérea', 'erigiré' o 'radar'.
# Implemente la función de forma que retorne un valor booleano (True si es un palíndromo y false en caso contrario).
# - Considere cómo eliminar los acentos para asegurarse tener comparaciones 1:1 correctas cono en el caso de las é en aérea y erigiré respectivamente.
# - Considere normalizar las mayúsculas y minúsculas


def es_palindromo(palabra: str) -> bool:
    #Implemente aquí su solución y retorne un valor boolean
    palabra = palabra.lower()
    palabra = remplazo_tilde(palabra)
    if(palabra[::-1] == palabra):
        return True
    return False
    
def remplazo_tilde(palabra: str) -> str:
    acentos: dict = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u'}
    palabra = palabra.lower()
    for acento in acentos:
        if acento in palabra:
            palabra = palabra.replace(acento, acentos[acento])
    return palabra

print(es_palindromo("aérea"))

# --------------------------------------------------------------------------------
# Unos amigos están cansados de enviarse mensajes de forma convencional ya que han visto que algunas personas están húsmeando sus conversaciones, por lo que decidieron cambiar el formato de los mensajes para que sea un poco más difícil de leerlos por personas que no son los que deberian recibir los mensajes. Para evitar esto, se requiere que programe una función que sea capaz de encriptar los mensajes que se envían por la aplicación y otra capaz de desencriptar para que los usuarios puedan leer los mensajes. Puede suponer que recibe hileras de caracteres sin valores numéricos.
# Escriba la función que, recibiendo por parámetro un arreglo de mensajes, encripta las vocales por números de forma que:
# a -> 1, e -> 2, i -> 3, o -> 4, u -> 5, A -> 6, E -> 7, I -> 8, O -> 9, U -> 0
# Por ejemplo, si la entrada es [“Hola", "MUNDO”], el resultado será: ['H4l1', 'm5nd4']

def encriptar(lista_palabras: list) -> list:
    #agregue aquí su código para encriptar y retorne una lista de datos encriptados
    vocales: dict = {
        'a':1,
        'e':2,
        'i':3,
        'o':4,
        'u':5,
        'A':6,
        'E':7,
        'I':8,
        'O':9,
        'U':0,
    }
    nueva_palabra: list = []
    for palabra in lista_palabras:
        for letra in vocales:
            if(letra in palabra):
                palabra = palabra.replace(letra, str(vocales[letra]))
        nueva_palabra.append(palabra)
    
    return nueva_palabra

print(encriptar(["Hola", "MUNDO"]))

# ----------------------------------------------------------------------------------------------
# Para finalizar nuestro programa, necesitamos que los amigos tengan una forma de convertir los mensajes de vuelta a texto plano para poder ser leidos desde cualquier lado. 
# Escriba la función que, recibiendo por parámetro un arreglo de mensajes, desencripta las vocales por números de forma que:
# 1 -> a, 2 -> e, 3 -> i, 4 -> o, 5 -> u, 6 -> A, 7 -> E, 8 -> I, 9 -> O, 0 -> U
# Por ejemplo, si la entrada es [“H4l1", "M0ND9”], el resultado será:  [“Hola", "MUNDO”]
def desencriptar(lista_palabra: list) -> list:
    #agregue aquí su código para desencriptar y retorne una lista de datos encriptados
    vocales: dict = {
        1:'a',
        2:'e',
        3:'i',
        4:'o',
        5:'u',
        6:'A',
        7:'E',
        8:'I',
        9:'O',
        0:'U',
    }
    nuevas_palabras: list = []
    for palabra in lista_palabra:
        for letra in vocales:
            if (str(letra) in str(palabra)):
                palabra = palabra.replace(str(letra), vocales[letra])
        nuevas_palabras.append(palabra)
    print("variables locales")
    print(locals()) # con locals se pueden ver todas las varibales locales de una funcion
    return nuevas_palabras

print(desencriptar(["H4l1", "M0ND9"]))
print("variables globales del programa")
print(globals()) # con globals se pueden ver todas las varibales globales del programa