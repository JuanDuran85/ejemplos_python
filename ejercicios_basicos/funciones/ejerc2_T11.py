# Crea una función lambda que dados dos números devuelva si el 
# primero es mayor.

print('------------------------------------------------------------------\n')
x=float(input('Introduzca un primer número:'))
y=float(input('Introduzca otro número para calcular cuál es el mayor:'))
numrs_mayor = (lambda x, y: x > y)
resultado= numrs_mayor(x,y)
print(x if resultado is True else '--> ERROR: El primer número ingresado no es el mayor.')
print('------------------------------------------------------------------')