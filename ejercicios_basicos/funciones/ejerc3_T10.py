# Crea una función que dado un número, devuelva su valor 
# absoluto. 
# Recuerda:
#          |x| =     x si x >= 0
#                   −x si x < 0

print('------------------------------------------------------------------')
def valor_abs(x):
    """
    Función para calcular el Valor Absoluto de un número, y mostrarlo. 
        
    Args: Un número real positivo, cero o negativo.
    
    Salida: Un número real positivo o cero.
    """
    if x >= 0:
        return print(f'El Valor Absoluto del número "{x}" es: {x}')
    else:
        x=(-1)*x
        return (f'El Valor Absoluto del número "-{x}" es: {x}')
print(valor_abs(float(input('Introduzca un número real para calcular su Valor Absoluto:'))))
print('------------------------------------------------------------------')
