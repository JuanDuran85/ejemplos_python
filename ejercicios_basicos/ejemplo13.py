# trabajando con funciones


def suma(a, b):
    return a + b

print(suma(2, 3))

# valores por defecto en funciones
def suma2(a:int=0, b:int=0) -> int:
    return a + b
print(suma2())


# funciones con argumentos variables
def suma3(*args):
    resultado = 0
    for i in args:
        resultado += i
    return resultado

print(suma3(1, 2, 3, 4, 5))

# Crear una función para multiplicar los valores recibidos de tipo numérico, utilizando argumentos variables *args como parámetro de la función y regresar como resultado la multiplicación de todos los valores pasados como argumentos.

def multiplica(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado

print(f"El resultado de la multiplicacion de: 1*2*3*4*5 es: {multiplica(1, 2, 3, 4, 5)}")

# pasando diccionaio como argumento
def suma4(**kwargs):
    resultado = 0
    for i in kwargs:
        resultado += kwargs[i]
    return resultado
print(suma4(a=1, b=2, c=3, d=4, e=5))

def listar_terminos(**kwargs):
    for i in kwargs:
        print(f"{i}: {kwargs[i]}")

listar_terminos(nombre="Juan", apellido="Perez", edad=25)

def listar_dicc(**kwargs):
    for llave,valor in kwargs.items():
        print(f"{llave}: {valor}")

listar_dicc(nombre="Juan", apellido="Perez", edad=25)

# recibir lista de elementos en una funcion
def lista_elementos(nombres):
    for i in nombres:
        print(i)

nombres = ['Juan','Elio','Pedro','Maria']
lista_elementos(nombres)
# si se envia un solo elemento del tipo string, lo itera como una lista
lista_elementos('Juan')
lista_elementos((10,20))
lista_elementos([-33, -44, -55])

# ------------ funciones recursivas ---------------
# calculando el factorial de un numero con funciones recursivas
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

resultado = factorial(5)
print(f"El factorial de 5 es: {resultado}")