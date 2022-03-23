"""_summary_

    La función reduce(): Aplica continuamente una misma función a los elementos de un objeto iterable
    1.- Aplica la función a los primeros dos elementos
    2.- Aplica la función al resultado del paso anterior y el tercer elemento
    3.- Aplica la función al resultado del paso anterior y el cuarto elemento
    4.- Sigue así hasta que solo queda un elemento
    5.- Devuelve el valor resultante

"""

# Con la ayuda de las funciones lambda, apliquemos reduce() para calcular 
# el producto de todos los elementos de una lista:
print('-----------------------------------------------------------1')
from functools import reduce

nums = [1, 2, 3, 4, 5, 6, 7]
print(reduce(lambda x, y: x * y, nums)) #Funcion Factorial


# De nuevo, la función proporcionada a reduce() no tiene por qué ser lambda,
# sino que puede ser una ya existente o bien, una creada por nosotros mismos.

# Con las siguientes líneas de código, vamos a obtener el máximo de una 
# lista dada, haciendo uso de reduce() y la función creada bigger_than():
print('-----------------------------------------------------------2')
def bigger_than(a, b):
    if a > b:
        return a
    return b
print(bigger_than(-141, 7))

# Con la función reduce() podemos aplicarla a una lista de números:
print('-----------------------------------------------------------3')
nums = [-100, 5, 7, -3, 46, -300, 29, 30]
print(reduce(bigger_than, nums))