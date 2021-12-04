# creamos una lista usando el range
numeros_listas = range(10)
lista_pares = []

# creamos una nueva lista con los valores pares multiplicados ṕor si mismo desde la lista anterior
for numero in numeros_listas:
    if numero % 2 == 0:
        lista_pares.append(numero*numero)
        print(numero)

print(lista_pares)

# Ahora trabajando el ejemplo anterior pero con list comprehensions
''' 
sintaxis de list comprehensions: 
    [<expresion> for <elemento> in <lista> if <condicion>]
la condicion if es opcional
'''
lista_pares_nueva = [numero for numero in range(10) if numero % 2 == 0]
print(lista_pares_nueva)

# se puede trabajar cuando existe dos condicion
lista = range(100)
lista_nueva = []
lista_nueva = [numero for numero in lista if numero %
               2 == 0 if numero % 3 == 0]
print(lista_nueva)

# agreando if else
numeros_pares = []
numeros_impares = []
[numeros_pares.append(numero) if numero % 2 == 0 else numeros_impares.append(
    numero) for numero in range(10)]
print(numeros_pares)
print(numeros_impares)

# lista de lista (matriz) para convertir en una sola lista
lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# convertir la lista de lista (matriz) en una sola
lista_simple = [valor for sublista in lista_de_listas for valor in sublista]
print(lista_simple)

# creando una lista de numeros pares per de una matriz
# primero sin list comprehensions. Utilizando ciclos for anidados
matriz3_3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pares = []
for sublista in matriz3_3:
    for valor in sublista:
        if valor % 2 == 0:
            pares.append(valor)

print(pares)

# ahora el ejemplo anterior usando list comprehensions
matriz3_3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
pares = [valor for sublista in matriz3_3 for valor in sublista if valor % 2 == 0]
print(pares)
