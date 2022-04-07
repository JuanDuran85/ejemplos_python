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

# funciones de primer orden
maximum = max
print(f"El maximo de los numeros 10, 20, 30 es: {maximum(10, 20, 30)}")

num_list = [10, 20, 30, 34, 45, 56, 67, 78, 89, 90]
print(f"El maximo de los numeros en la lista es: {maximum(num_list)}")

# funciones como ciudadanos de primera clase

def calcule_gst(price, type_of_item):
    if type_of_item == "Product":
        return price * 1.05
    elif type_of_item == "Service":
        return price * 1.18
    
    return price * 1.35

def calcule_vat(price, type_of_item):    
    return price * 1.2
# las funciones como ciudadanos de primera clase se pueden asignar a variables
type_of_tax = calcule_gst
print(f"El precio con GST es: {type_of_tax(1000, 'Product')}")
print(f"El precio con GST es: {type_of_tax(1000, 'Service')}")

# se puede retornar una funcion de otra funcion porque son ciudadanos de primera clase

def find_tax_calculator(type_of_tax):
    if type_of_tax == "GTS":
        return calcule_gst
    elif type_of_tax == "VAT":
        return calcule_vat
    return 'No existe la calculadora para ese impuesto'

gst_fn = find_tax_calculator("GTS")
print(f"El precio con GST es: {gst_fn(1000, 'Product')}")
print(f"El precio con GST es: {gst_fn(1000, 'Service')}")

vat_fn = find_tax_calculator("VAT")
print(f"El precio con VAT es: {vat_fn(1000, 'Product')}")
print(f"El precio con VAT es: {vat_fn(1000, 'Service')}")

# -------------------------------------------------------------------------------------
def es_bisiesto(anyo: int) -> bool:
    #Programe su solución aquí
    if anyo % 4 == 0 and anyo > 0:
        if anyo % 100 == 0:
            if anyo % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False
print(es_bisiesto(-2020))

def encontrar_mayor(a: int, b: int, c: int) -> int:
    lista: list = []
    lista.append(a)
    lista.append(b)
    lista.append(c)
    return max(lista)
    
print(encontrar_mayor(5,22,5))

# con for
def determinar_primo(numero: int) -> bool:
    #Implemente su solución aquí
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    for i in range(2, numero):
        if (numero % i == 0):
            return False
        return True
        
print(determinar_primo(2))

# con while
def es_primo(numero: int) -> bool:
    contador: int = 2
    
    if (numero < 2):
        return False
    
    while(contador <= numero**(1/2)):
        if(numero % contador == 0):
            return False
        contador += 1
    
    return True

for i in range(1,101):
    print(f"{i} - {es_primo(i)}")