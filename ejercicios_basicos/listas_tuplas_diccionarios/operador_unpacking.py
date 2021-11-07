# trabajando con el operador unpacking
numeros = [1, 2, 3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')

# trabajando con operador unpacking en funciones

def sumas(a,b,c):
    print(f"La suma de {a} + {b} + {c} es: {a+b+c}")

sumas(*numeros)

# extraer algunos valores (partes) de una lista
mi_lista = list(range(1,7))
print(mi_lista)
a,*b,c = mi_lista
print(a, b, c)

# creando listas con el operador unpacking
lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = [*lista1, *lista2]
print(lista3)

# unir diccionarios con el operador unpacking
diccionario1 = {'a':1, 'b':2, 'c':3}
diccionario2 = {'d':4, 'e':5, 'f':6}
diccionario3 = {**diccionario1, **diccionario2}
print(diccionario3)

# construir una lista a partir de un string
lista_string = [*"NuevaListaParaMostrar"]
print(lista_string)
print(*lista_string, sep='')