"""_summary_

    La funcion Map posee las siguientes caracteristicas:
        1.- Aplica una misma función a todos los elementos de un objeto iterable
        2.- Devuelve un objeto generador, de ahí que usemos la función list() 
            para convertirlo a lista 
        3.- Como output, devuelve el resultado de aplicar la función a cada elemento

"""

# Con la ayuda de las funciones lambda, apliquemos map() para calcular las longitudes de las siguientes palabras:

print('-----------------------------------------------------------1')

words = ["zapato", "amigo", "yoyo", "barco", "xilófono", "césped"]
print(list(map(lambda w: len(w), words)))

# OJO: Sin embargo, para este caso en concreto no haría falta usar funciones lambda, pues podríamos hacer directamente:
print('-----------------------------------------------------------2')
print(list(map(len, words)))

# utilizando una funcion que retorne el doble del numero ingreso proveniente de una lista, implementar la funcion map()
print('-----------------------------------------------------------2')
numeros_lista: list = [3,5,7]
print(f"{numeros_lista = }")
resultado: list = list(map(lambda x: x*2, numeros_lista))
print(f"{resultado = }")
 