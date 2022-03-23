"""_summary_

    La funcion Map posee las siguientes caracteristicas:
        1.- Aplica una misma función a todos los elementos de un objeto iterable
        2.- Devuelve un objeto generador, de ahí que usemos la función list() 
            para convertirlo a lista 
        3.- Como output, devuelve el resultado de aplicar la función a cada elemento
        
    Python map function is used to execute a function on all elements of an iterator. The
    function to execute will be passed to map() as a parameter.
    
        map(function, iterators)
        
        1.- function: Required and will execute for items of iterators
        2.- iterators: Required. You can send many iterators. However, the function must have
        one parameter for each iterator.
"""

# Con la ayuda de las funciones lambda, apliquemos map() para calcular las longitudes de las siguientes palabras:

print('-----------------------------------------------------------')

words = ["zapato", "amigo", "yoyo", "barco", "xilófono", "césped"]
print(list(map(lambda w: len(w), words)))

# OJO: Sin embargo, para este caso en concreto no haría falta usar funciones lambda, pues podríamos hacer directamente:
print('-----------------------------------------------------------')
print(list(map(len, words)))

# utilizando una funcion que retorne el doble del numero ingreso proveniente de una lista, implementar la funcion map()
print('-----------------------------------------------------------')
numeros_lista: list = [3,5,7]
print(f"{numeros_lista = }")
resultado: list = list(map(lambda x: x*2, numeros_lista))
print(f"{resultado = }")

# A partir de una lista de numeros, obtenga una lista con los numeros incrementados en 10 utilizando la funcion map()
print('-----------------------------------------------------------')
lista_numeroa: list = list(range(1,11))
resultado_numeros: list = list(map(lambda x: x+10, lista_numeroa))
print(f"{resultado_numeros = }")

#---------------------------------------------------------------------------------------
print('----------------------------------------')
print("\r\nPassing multiple Iterators to map() function")
print("Lambda function should have one parameter for each iterator.")
iterator_one: list = [1,5,7]
iterator_two: list = [9,5,3]
print(f"{iterator_one = }")
print(f"{iterator_two = }")
result_map: list = list(map(lambda x,y: x+y, iterator_one, iterator_two))
print(f"{result_map = }")

#---------------------------------------------------------------------------------------
print('----------------------------------------')
print("\r\nPassing multiple Iterators with diﬀerent size")
print("Let's see what happen if we pass multiple iterators with diﬀerent size. In python 2, we got an exception. Therefore, be aware of this case in your code. In python 3, we get a map object with the size of smallest iterator.")

list_one: list = [1,5,7,9,8]
list_two: list = [9,5,3]
print(f"{list_one = }")
print(f"{list_two = }")

result_map: list = list(map(lambda x,y: x+y, list_one, list_two))
print(f"{ result_map = }")
