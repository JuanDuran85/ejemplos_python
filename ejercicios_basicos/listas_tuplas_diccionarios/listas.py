# obtener el indice del primer elemento encontrado en una lista
numeros = [11,20,3,34,15,6,87,18,-9,10]
print(f"Lista original: {numeros}")
print(f"Indice del numero 18: {numeros.index(18)}")

# invertir el orden de los elementos de una lista
numeros.reverse()
print(f"Lista invertida: {numeros}")

# ordenar los elementos de una lista
numeros.sort()
print(f"Lista ordenada: {numeros}")

# ordenar de menera descendente los elementos de una lista
numeros.sort(reverse=True)
print(f"Lista ordenada de forma descendente: {numeros}")

# obtener valor maximo y minimo de una lista
print(f"Valor maximo: {max(numeros)}")
print(f"Valor minimo: {min(numeros)}")

# copiando elementos de una lista a otra
# usando el metodo copy() el cual entrega las referencias a los elementos (realiza copia superficial)
numeros_copia = numeros.copy()
print(f"Lista copiada: {numeros_copia}")
print(f"Es la misma referencia: {numeros is numeros_copia}")
print(f"Mismo contenido: {numeros == numeros_copia}")

# usando el constructor de listas de python list()
numeros_copia2 = list(numeros)
print(f"Lista copiada: {numeros_copia2}")
print(f"Es la misma referencia: {numeros is numeros_copia2}")
print(f"Mismo contenido: {numeros == numeros_copia2}")

# usando slicing recorriendo la lista de inicio a fin
numeros_copia3 = numeros[:]
print(f"Lista copiada: {numeros_copia3}")
print(f"Es la misma referencia: {numeros is numeros_copia3}")
print(f"Mismo contenido: {numeros == numeros_copia3}")

# multiplicacion de listas de listas
lista_multiplicada = 5*[[5,2]]
print(f"Lista multiplicada: {lista_multiplicada}")
print(f"Es la misma referencia: {lista_multiplicada[0] is lista_multiplicada[1]}")
print(f"Mismo contenido: {lista_multiplicada[0] == lista_multiplicada[1]}")
# como tienen la misma referencia, al modificar un elemento de la lista todos seran modifcados por referencia
lista_multiplicada[3].append(3)
print(f"Lista multiplicada: {lista_multiplicada}")

# trabajando con matrices en python (listas de listas)
matriz = [[31,12,-3],[-4,25,16],[87,8,69]]
print(f"Matriz original: {matriz}")
# accediendo a un elemento de la matriz
print(f"Elemento de la matriz[1][2]: {matriz[1][2]}")
print(f"Elemento de la matriz[0][1]: {matriz[0][1]}")
print(f"Elemento de la matriz[2][0]: {matriz[2][0]}")