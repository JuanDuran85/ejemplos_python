# Crea una función lambda que dado un número entero multiplique por 
# su anterior y su siguiente. Por ejemplo, si proporcionamos n = 3,
# nos tendrá que devolver 2 · 3 · 4 = 24.

print('------------------------------------------------------------------')
n=int(input('Introduzca en número entero positivo: '))
valor=lambda x: x*(x-1)*(x+1)
print(f'El num. ingresado fue el "{n}"; y el resultado de multiplicar por su anterior y su posterior es: ')    
print(valor(n))
print('------------------------------------------------------------------')