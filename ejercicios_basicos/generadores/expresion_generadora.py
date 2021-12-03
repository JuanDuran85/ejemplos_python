import math

# Expresion generadora (es un generador anonimo)

multiplicar = (valor*valor for valor in range(6))
print(type(multiplicar))
print(next(multiplicar))
print(next(multiplicar))
print(next(multiplicar))
print(next(multiplicar))
print(next(multiplicar))
print(next(multiplicar))


# tambien se puede pasar una funcion generadora a una funcion sin parentisis
suma = sum(valor*valor for valor in range(6))
print(type(suma))
print(suma)

# Usando lista con generador
lista = ['Juan', 'Pedro', 'Maria', 'Ana']
generador = (nombre for nombre in lista)
print(type(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

# crear un string a partir de un generador que es creado a partir de una lista
lista = ['Juan', 'Pedro', 'Maria', 'Ana']
contador = 0

# definir funcion que permita incremenentar la variable contador
def incrementar_contador():
    global contador
    contador += 1
    return contador

# crear expresion generadora
# la primera parte es el yield, la segunda pate es el for, entre parentesis

generador = (f'{incrementar_contador()}.- {nombre}' for nombre in lista)

# crear una lista a partir del generador
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(cadena)
