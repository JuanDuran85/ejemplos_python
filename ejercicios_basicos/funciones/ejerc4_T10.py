# Crea una función que devuelva True si el caracter introducido
# por parámetro se trata de una vocal, y False en caso contrario.

print('------------------------------------------------------------------')
def detectar_vocal(letra):
    """
    Función para validar si el caracter introducido es una vocal, y mostrarlo. 
        
    Args: Un caracter.
    
    Salida: True (si es una vocal), False si no es una vocal.
    """
    vocal=('a','e','i','o','u')
    for index in vocal:
        if  index==letra:
            return ('True: El caracter introducido es una vocal.')
    else:
        return ('False: El caracter introducido NO es una vocal.')
print(detectar_vocal(str(input('Introduzca un caracter para calcular si es o no una vocal:'))))
print('------------------------------------------------------------------')


