"""_summary_

    Usando doctest para testear una función basica.
    
    para ejecutar la prueba, se debe agregar el -v al final del nombre del archivo en la terminal

"""

import doctest

def sumar(num1: int, num2: int) -> int:
    """
        Documentacion de la funcion
        Funcion Sumar: recibe dos numeros y retorna la suma
        >>> sumar(1, 2)
        3
        
        >>> sumar(4, 2)
        6
        
        >>> sumar(3, 5)
        8
    """
    return num1 + num2

resultado: int = sumar(2,3)
print(f"{ resultado = }")

doctest.testmod()