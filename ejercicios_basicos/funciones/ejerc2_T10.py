# Crea una función que dados dos números reales por 
# parámetro, devuelve número mayor.  

print('------------------------------------------------------------------\n')
def divisores_xy(x,y):
    """
    Función para calcular entre dos números, el mayor y mostrarlo. 
        
    Args: Dos números reales.
    
    Salida: número real mayor de los dos introducidos.
    """
    if x > y:
        return (f'\nEntre los dos números ingresados {x} y {y}; el número mayor es el: {x}.')
    elif x < y:
        return (f'\nEntre los dos números ingresados {x} y {y}; el número mayor es el: {y}.')
    elif x == y:
        return (f'** Los dos números ingresados son iguales.\n')
print(divisores_xy(float(input('Introduzca un primer número:')),float(input('Introduzca otro número para calcular cúal es el mayor:'))))
print('------------------------------------------------------------------')