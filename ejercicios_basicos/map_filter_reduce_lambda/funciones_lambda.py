"""_summary_

    Trabajando con funciones lambda: es una funcion anonima y pequeña (una linea de codigo). Se usa la palabra reservada lambda, los parametros son opcionales.
    
    What Is Lambda Function: A lambda function is an anonymous function. In Python, an anonymous function is a function without a name. A normal function will start by def keyword. An anonymous function deﬁnes by the lambda keyword, therefore we usually call them as a lambda function.

"""

mi_funcion_lambda = lambda a,b: a+b
print(f"La suma es: {mi_funcion_lambda(22,53)}")

mi_funcion_lambda = lambda x: x**2
print(f"El cuadrado es: {mi_funcion_lambda(5)}")

# una funcion lambda que no recibe argumentos pero debe regresar una expresion valida
mi_funcion_lambda = lambda: "Funcion lambda sin argumentos..."
print(mi_funcion_lambda())

# asignando valores por defecto a argumentos de una variable lambda
mi_funcion_lambda = lambda a=2,b=5: a+b
print(f"La suma es: {mi_funcion_lambda()}")

mi_funcion_lambda = lambda x=2: x**2
print(f"El cuadrado es: {mi_funcion_lambda()}")

# funcion lambda con argumentos variables *args(tuplas) y **kwargs(diccionarios)
mi_funcion_lambda = lambda *args, **kwargs: print(args, kwargs)
mi_funcion_lambda(1,5,3,2, a=5,b=34)
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(mi_funcion_lambda(1,5,3,2, a=5,b=34))

# funciones lambda con argumentos, argumentos varibales y valores por defecto
mi_funcion_lambda = lambda x,y,z=4,*args, **kwargs: x+y+z+len(args)+len(kwargs)
print(mi_funcion_lambda(1,5,3,2,5,-6, r=5,w=34))

# utilizando funciones lambda

# el doble del numero enviado
doblar_numero = lambda num: num * 2
print(f"{doblar_numero(25) = }")

# numero impar
impar = lambda num: num % 2 != 0
print(f"{impar(2) = }")

# revertir cadena
revertir_cadena = lambda texto: texto[::-1]
print(f"{revertir_cadena('hola') = }")

# sumar dos numeros
sumar_numeros = lambda num1,num2: num1 + num2
print(f"{sumar_numeros(5,6) = }")


# -------------------------------------------------------------------------------------------------
print("\n------------------------------------------\n")
# Lambda function with only 1 argument
print("Lambda function with only 1 argument")
result_double: int = lambda x: x*2
print(f"{result_double(5) = }")

# Lambda function with multiple arguments
print("Lambda function with multiple arguments")
sum_tow_numbers: int = lambda x,y: x+y
print(f"{sum_tow_numbers(5,6) = }")

# Lambda And Map Function
print("Lambda And Map Function")
list_one: list = [1,2,3,4,5,6,7,8,9,10]
list_two: list = [6,2,-8,-2,-1,0,3,6,9]
print(f"{list_one = }")
print(f"{list_two = }")
result_lambda_map: list = list(map(lambda x,y: x+y, list_one, list_two))
print(f"{result_lambda_map = }")

# Lambda And Filter Function
print("Lambda And Filter Function")
data_list: range = range(-6,6)
print(f"{data_list = }")

greater_then_zero: list = list(filter(lambda x: x > 0, data_list))
print(f"{greater_then_zero = }")

# Find Factorial of a Number with lambda

factorial_number = lambda num: 1 if num <= 1 else num*factorial_number(num-1)

print(f"{factorial_number(3) = }")
print(f"{factorial_number(6) = }")
print(f"{factorial_number(9) = }")
print(f"{factorial_number(13) = }")

# ---------------------------------------------------------------------------------
# Quicksort with Lambda and list comprehension
list_number: list = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
sorted_list = lambda list_of_number: sorted_list([x for x in list_of_number[1:] if x <= list_of_number[0]])+ [list_of_number[0]] + sorted_list([x for x in list_of_number if x > list_of_number[0]]) if list_of_number else []
print(f"{sorted_list(list_number) = }")

# Fibonacci with Lambda
fibonacci_function = lambda x: x if x<= 1 else fibonacci_function(x-1) + fibonacci_function(x-2)
print(f"{fibonacci_function(7) = }")
