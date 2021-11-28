# Crea una función que dado un string por parámetro cuente
# cuántas veces sale cada caracter en dicho string y 
# devuelva toda esa información en un diccionario.
print('------------------------------------------------------------------\n')
def string_palabra(palabra):
    """
    Función para recibir un un string o palabras y detectar cuantas veces exite
    cada letra en la expresión introducida.
    
    Args: Lista de palabras o expresion.
    
    Salida: Diccionario con cada letra y las cantidades de veces en la expresión
    introducida.
    """
    palabra=palabra.lower()
    palabra=list(palabra)
    dicc, letra=[],[]
    if len(palabra)>0:    
        for letra in palabra:
            n= palabra.count(letra)
            dicc.append((letra,n))
        dicc=dict(dicc)
        print(dicc)
string_palabra(input("Introduce una frase o palabras:\n "))
print('------------------------------------------------------------------')