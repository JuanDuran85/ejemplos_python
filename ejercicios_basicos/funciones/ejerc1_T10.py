# Crea una función que busque todos los divisores del número
# entero positivo dado por parámetro y devuelva una lista 
# con todos los divisores de dicho número.

print('------------------------------------------------------------------')
def divisores_n(n):
    """
    Función para calcular los divisores del número entero y mostrar 
    lista con los divisores.
    
    Args: número "n" entero positivo.
    
    Salida: lista con todos los divisores de dicho número "n".
    """
    lista=[]
    for i in range(1,n+1):
        if n % i ==0:
            lista.append(i) 
    return (f'La lista de divisores del número ingresado es: {lista} ')
print(divisores_n(int(input('Introduzca un número entero para calcular sus divisores:'))))
print('------------------------------------------------------------------')