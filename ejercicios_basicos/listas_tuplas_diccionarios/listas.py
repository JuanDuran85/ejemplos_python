# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

"""_summary_

    List methods

"""
LINES = "---------------------------------------------------------------------\r\n"

# obtener el indice del primer elemento encontrado en una lista
numeros = [11, 20, 3, 34, 15, 6, 87, 18, -9, 10]
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
lista_multiplicada = 5*[[5, 2]]
print(f"Lista multiplicada: {lista_multiplicada}")
print(f"Es la misma referencia: {lista_multiplicada[0] is lista_multiplicada[1]}")
print(f"Mismo contenido: {lista_multiplicada[0] == lista_multiplicada[1]}")
# como tienen la misma referencia, al modificar un elemento de la lista todos seran modifcados por referencia
lista_multiplicada[3].append(3)
print(f"Lista multiplicada: {lista_multiplicada}")

# trabajando con matrices en python (listas de listas)
matriz = [[31, 12, -3], [-4, 25, 16], [87, 8, 69]]
print(f"Matriz original: {matriz}")
# accediendo a un elemento de la matriz
print(f"Elemento de la matriz[1][2]: {matriz[1][2]}")
print(f"Elemento de la matriz[0][1]: {matriz[0][1]}")
print(f"Elemento de la matriz[2][0]: {matriz[2][0]}")
# modificando elementos en una matriz
matriz[0][1] = -5
print(f"Matriz modificada: {matriz}")

# ordenando una matriz en python
matriz2 = [[3, 2, 6, 24, 67, -3], [4, -5, 0, 16], [8, -8, -6]]
print(f"Matriz original: {matriz2}")
matriz2.sort(key=len)
print(f"Matriz ordenada: {matriz2}")

# ordenando matrices con built-in que ya son parte de python "sorted()"
matriz3 = ["Juan", "Yecelis", "Mariana", "Elio", "Yecenia", "Ali"]
print(f"Matriz original: {matriz3}")
matriz3 = sorted(matriz3)
print(f"Matriz ordenada: {matriz3}")
matriz3 = sorted(matriz3, reverse=True)
print(f"Matriz ordenada: {matriz3}")
# ordenando por la cantidad de caracterese de cada elemento
matriz3 = sorted(matriz3, key=len)
print(f"Matriz ordenada: {matriz3}")

# build-in reverse(), permite trabajar con cualquier iterable
matriz4 = ["Juan", "Yecelis", "Mariana", "Elio", "Yecenia", "Ali"]
print(f"Matriz original: {matriz4}")
matriz4 = reversed(matriz4)
print(f"Matriz invertida: {list(matriz4)}")


# ----------------------------------------------------------------------------------------
print(LINES)
print(LINES)
print("Using list slicing to access, modify, and manipulate portions of a list")
# syntax: list[start:stop:step], where start, stop, and step are optional parameters.
# start: The index where the slice begins (inclusive). If omitted, defaults to 0 (the beginning of the list).
# stop: The index where the slice ends (exclusive). If omitted, defaults to the length of the list (the end).
# step: The increment between elements. If omitted, defaults to 1. A negative step means slicing in reverse.
list_to_work: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

print("1. Extracting Sub-Lists (The Most Common Use)")

print(list_to_work[2:6])  # Slicing from start to stop (basic range)
print(list_to_work[:5])  # Slicing from the beginning to stop
print(list_to_work[5:])  # Slicing from start to the end

copy_list_to_work: list[int] = list_to_work[:]  # Copying the entire list (shallow copy)
print(f"{copy_list_to_work=}")

print("2. Using Negative Indices")
# Negative indices count from the end of the list. -1 is the last element,
# -2 is the second to last, and so on.
print(f"{list_to_work[-3:-1]}")  # Slicing from a negative start to a negative stop
print(f"{list_to_work[-3:]}")  # Slicing from a negative start to the end
print(f"{list_to_work[:-2]}")  # Slicing from the beginning to a negative stop
print(f"{list_to_work[2:-3]}")  # Mixing positive and negative indices

print("3. Slicing with step")  # The step parameter allows you to skip elements.
print(f"{list_to_work[::3]}")  # Taking every Nth element
print(f"{list_to_work[::2]}")  # Taking every Nth element
print(f"{list_to_work[1:10:2]}")  # Slicing with a start, stop, and step
print(f"{list_to_work[::-1]}")  # Reversing a list
print(f"{list_to_work[7:1:-1]}")  # Reversing a portion of a list
print(f"{list_to_work[:-4:-1]}")  # Reversing a portion of a list

print("4. Modifying Lists with Slices")
# Replacing a slice with new elements
# The number of elements in the assigned iterable does not have to match the size of the slice being replaced.
list_to_work_ii: list[int | str] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
list_to_work_ii[1:3] = ["a", "b", "c"]
print(f"{list_to_work_ii=}")

# Inserting elements using a zero-length slice
# f start and stop are the same, the slice is empty, and assigning to it inserts elements at that position.
list_to_work_ii[1:1] = ["A", "B"]
print(f"{list_to_work_ii=}")

#  Clearing a portion of a list (assigning an empty list)
list_to_work_ii[1:6] = []
print(f"{list_to_work_ii=}")

print("5. Deleting Elements with Slices (using del)")
# The del statement combined with slicing provides a way to remove multiple elements efficiently.
list_to_work_iii: list[int | str] = [3, 5, 6, 2, 8, 4, 78, 31, 89, 1, 0, -1]

# Deleting a range of elements
del list_to_work_iii[1:4]
print(f"{list_to_work_iii=}")

# Deleting elements with a step
del list_to_work_iii[::3]  # Deletes every third element
print(f"{list_to_work_iii=}")

# Clearing the entire list
del list_to_work_iii[:]
print(f"{list_to_work_iii=}")


print("6. Slicing with Out-of-Bounds Indices")
# Python's slicing is forgiving. If a start or stop index is out of bounds,
# it simply clips to the beginning or end of the list without raising an error.
list_to_work_iV: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(f"{list_to_work_iV[0:100]}")  # Slicing from the beginning to an out-of-bounds index, goes to end of list
print(f"{list_to_work_iV[-40:3]}")  # starts from beginning, goes to index 3
print(f"{list_to_work_iV[20:]}")  # empty list as nothing beyond end

print(LINES)
# ----------------------------------------------------------------------------------------
