# Crea una función que devuelva el MCM (mínimo común múltiplo) 
# de dos números proporcionados por parámetro.
# PISTA: Aprovecha la función que calcula el MCD de dos números del 
# ejercicio anterior y la función que calcula el valor absoluto de
# un número.

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
    return mcd  

# Formula para el Máximo Común Múltiplo: MCM (x,y) = |x*y| / MCD (x,y) 
def mcm_xy(x,y):
    if x < 0:
        x=(-1)*x
    if y < 0:
        y=(-1)*y
    val_abs= x*y
    mcc=int(val_abs/mcd_xy(x,y))
    return (f'El Mínimo Común Múltiplo entre {x} y {y} es: {mcc} ')
print(mcm_xy(int(input('Introduzca un primer número:')),int(input('Introduzca otro número diferente de cero para calcular el MCM:'))))
print('------------------------------------------------------------------')
