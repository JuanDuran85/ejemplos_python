# Crea una función que dada una palabra devuelva si es
# palíndroma.

print('------------------------------------------------------------------')
def palindroma(palabra):
    """
    Función para detectar palabras palíndromas.
    
    Args: palabra.
    
    Salida: Confirmación si la palabra introducida es palíndroma (o no).
    """
    palabra=palabra.lower()
    palabra_inv = palabra[::-1]
    if palabra_inv  == palabra :
        return print(f'La palabra introducida "{palabra}"  es palíndroma' ) 
    else:
        return print(f'La palabra introducida "{palabra}" NO es palíndroma' )
palindroma(str(input("Introduce una frase o expresión: \n")))
print('------------------------------------------------------------------')
