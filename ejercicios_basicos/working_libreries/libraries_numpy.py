# trabajando con la libreria numpy

import numpy as np

some_list = [1,2,3,4,5,6,7,8,9,10]
print(type(some_list))

some_array = np.array(some_list)
print(type(some_array))

# el metodo cumsum suma y acumula los valores presentes en una lista
# the cumsum method sums and accumulates the values ​​present in a list
rest_sum = list(np.cumsum(range(0,10,2)))
print(f"{rest_sum = }")

# Creando un array con ceros
print(f"{np.zeros(4) = }")
# creando un array con unos
print(f"{np.ones(4) = }")
# creando un array de elementos
print(f"{np.arange(0,10,2) = }")
print(f"{np.arange(2,20,3) = }")
# creando un array a partir de otra
lista_nuermos_uno: list = [3,56,5,2]
array_uno: np.ndarray = np.array(lista_nuermos_uno)
print(f"{array_uno = }")
# creando un array a partir de dos listas
lista_nuermos_uno: list = [3,56,5,2]
lista_nuermos_dos: list = [8,6,3,1]
lista_doble: tuple= (lista_nuermos_uno, lista_nuermos_dos)
print(f"{lista_doble = }")
array_doble: np.ndarray = np.array(lista_doble)
print(f"{array_doble = }")
# para mostrar la forma que tiene un array en numpy
print(f"{array_doble.shape = }")
# para ver el tipo de dato que tiene el array
print(f"{array_doble.dtype = }")

# operaciones con array en numpy
array_uno: np.ndarray = np.array([1,2,3,4,5])
array_dos: np.ndarray = np.array([8,1,3,5,2])
# suma
print(f"{array_uno + array_dos = }")
# resta
print(f"{array_uno - array_dos = }")  # type: ignore
# multiplicacion
print(f"{array_uno * array_dos = }")
# division
print(f"{array_uno / array_dos = }")
# potencia
print(f"{array_uno ** 2 = }")

#-----------------------------------------------------------------------------
print("---------------------------------------------------------------------\r\n")
# indexacion con arrays en numpy
array: np.ndarray = np.arange(0,11)
print(f"{array = }")
# posicion inicial hasta una final
print(f"{array[2:5] = }")
# mostrar el array original y completo con :
print(f"{array[:] = }")
# creando una copia del array sin problemas de mutacion
array_copia: np.ndarray = array.copy()
print(f"{array_copia = }")
# modificando valores de una array por referencia
array_copia[:3] = 9
print(f"{array_copia = }")

#-----------------------------------------------------------------------------
print("\r\n---------------------------------------------------------------------\r\n")
# matrices y acceso a sus elementos en numpy
array_matriz: np.ndarray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"{array_matriz = }")
print(f"{array_matriz[0,2] = }")
# creando una matriz con 3 filas y 5 columnas mediante el metodo reshape
matriz_uno = np.arange(15).reshape(3,5)
print(f"{matriz_uno = }")
# matrices transpuestas
matriz_traspuesta = matriz_uno.T
print(f"{matriz_traspuesta = }")

#-----------------------------------------------------------------------------
print("\r\n---------------------------------------------------------------------\r\n")
# entrada y salida de arrays en numpy
array_uno: np.ndarray = np.arange(6)
print(f"{array_uno = }")
# salvando un array en numpy como archivo binario
np.save("array_uno_salvado", array_uno)
# cargando un array salvado en numpy
array_salvado: np.ndarray = np.load("array_uno_salvado.npy")
print(f"{array_salvado = }")
# salvando dos arreglos al mismo tiempo como binario
array_uno: np.ndarray = np.arange(6)
print(f"{array_uno = }")
array_dos: np.ndarray = np.arange(5,11)
print(f"{array_dos = }")
np.savez("array_dos_salvado", x=array_uno, y=array_dos)
# recuperando arrays salvados
savados_dos: np.ndarray = np.load("array_dos_salvado.npz")
print(f"{savados_dos['x'] = }")
print(f"{savados_dos['y'] = }")
# salvando arreglos como ficheros de texto
np.savetxt("array_savado_texto.txt", array_uno,delimiter=",")
# recuperando el archivo de texto guardado
array_texto = np.loadtxt("array_savado_texto.txt", delimiter=",")
print(f"{array_texto = }")

print("--------------------------------------------------------------------")
# funciones en arrays
# retornando al raiz cuadrada de cada uno de los elementos de un arreglo
array_nuevo: np.ndarray = np.arange(5)
print(f"{array_nuevo = }")
print(f"{array_nuevo ** 0.5 = }")
print(f"{np.sqrt(array_nuevo) = }")

# creando array de forma aleatoria
array_random: np.ndarray = np.random.rand((5))
print(f"{array_random = }")

# se pueden sumar dos arreglos con add de numpy
array_uno: np.ndarray = np.array([1,2,3,4,5])
array_dos: np.ndarray = np.array([4,6,1,2,9])
print(f"{array_uno + array_dos = }")
suma_arrays: np.ndarray = np.add(array_uno, array_dos)
print(f"{suma_arrays = }")
# para mostrar solo los valores maximos entre dos arrays columna a columna
maximos: np.ndarray = np.maximum(array_uno, array_dos)
print(f"{maximos = }")

#