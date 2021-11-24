# Crea una función que dada una lista de palabras por parámetro, 
# devuelva un diccionario que contenga cuántas son de longitud 
# par y cuántas de longitud impar.

print('------------------------------------------------------------------')
def palabra_par_impar(palabras):
    """
    Función para recibir una expresión o palabras y descriminar las apres
    e impares.
    
    Args: Lista de palabras o expresion.
    
    Salida: Diccionario con palabras de longitud par y de longitud impar.
    """
    palabras=palabras.lower()
    palabras=palabras.split()
    par, impar=[],[]
    n, m = 0,0
    for i in palabras:
        if len(i)%2==0:
            par.append(i)
            n=len(par)
        else:
            impar.append(i)
            m=len(impar)
    print(f'El total de palabras pares es: "{n}", y ellas son:{par} ')
    print(f'El total de palabras impares es: "{m}", y ellas son:{impar} ')
palabra_par_impar(input("Introduce una frase o palabras: \n"))
print('------------------------------------------------------------------')