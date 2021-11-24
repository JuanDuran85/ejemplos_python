# Crea una función que devuelva el MCD (máximo común divisor) de dos
# números proporcionados por parámetro.
# PISTA: Aprovecha la función que calcula el mayor entre dos números
# dados. También necesitarás una función que calcula el menor entre
# dos números dados.

print('------------------------------------------------------------------')
def mcd_xy(x,y):
    """
    Función para calcular el MCD (máximo común divisor) de 2 números y mostrar.

    Args: 2 números reales

    Salida: El MCD (máximo común divisor) de los 2 números introducidos.
    """
    lista1,  lista2,  lista3= [], [], []
    if x < 0:
        x=(-1)*x
    if y < 0:
        y=(-1)*y
    for i in range(1,x+1):
        if x % i ==0:
            lista1.append(i) 
    for i in range(1,y+1):
        if y % i ==0:
            lista2.append(i)         
    for i in lista1:
        for j in lista2:
            if i==j:
                lista3.append(i) 
        mcd=max(lista3)  
    return (f'El Máximo Común Divisor entre {x} y {y} es: {mcd} ')  

print(mcd_xy(int(input('Introduzca un primer número:')),int(input('Introduzca otro número diferente de cero para calcular el MCD:'))))