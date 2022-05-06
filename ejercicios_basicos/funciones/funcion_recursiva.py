# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas. Puede ser cualquier valor positivo, ejemplo, si pasamos el valor de 5, debe imprimir: 5 4 3 2 1 Si se pasa el valor de 3, debe imprimir: 3 2 1 Si se pasan valores negativos no imprime nada

def mostrar_numeros(numero):
    if numero > 0:
        print(numero)
        mostrar_numeros(numero - 1)

mostrar_numeros(3)


# ---------------------------------------------------------------------------------
# Crear una función para calcular el total de un pago incluyendo un impuesto aplicado.
# La función debe recibir una cantidad de dinero y un porcentaje de impuesto como parámetros.
# La función debe retornar el total del pago, incluyendo el impuesto.

def calcular_impuesto(dinero, porcentaje):
    impuesto = dinero * (porcentaje/100)
    return dinero + impuesto

sub_total = float(input("Ingrese su sub total a pagar: "))
impuesto = float(input("Ingrese el porcentaje de impuesto a aplicar: "))
print(calcular_impuesto(sub_total, impuesto))

total = 0
def calcula_impuesto(*dineros,impuesto):
    sub_total = 0
    for i in dineros:
        sub_total += i
    total = sub_total + (sub_total * impuesto)
    return total

total = calcula_impuesto(1,1,1,1,1, impuesto=0.16)
print(total)

# Funciones recursivas

def recursiveness_func(x,ans):
    if(x==0):
        return 0
    else:
        return recursiveness_func(x-1,x+ans)
print(recursiveness_func(2,66))

# ---------------------------------------------------------------------------------
# Una funcion recursiva es una funcion que se utiliza a si misma para resolver un problema.
def cuenta_atras(num: int) -> None:
    num -= 1
    if num > 0:
        print(f"{num = }")
        cuenta_atras(num)
    else:
        print(f"{num = }")
        print("Fin de la funcion")
    
cuenta_atras(10)

# factorial de un numero con funciones recursivas

def factorial_numero(num):
    if num > 1:
        num = num * factorial_numero(num - 1)
    return num
    
print(f"{factorial_numero(5) = }")

# ---------------------------------------------------------------------------------
# con una funcion recursiva, imprimir de forma descendente los numeros desde el mayor numero ingresado hasta 1. Si son valores negativos, no se debe imprimir nada.

def imprimir_numero(numero: int) -> str:
    if numero > 0:
        print(numero)
        return imprimir_numero(numero - 1)
        
print(imprimir_numero(10))