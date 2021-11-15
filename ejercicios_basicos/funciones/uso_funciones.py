# las funciones en python son ciudadanos de primera clase (FCC)
# First Class Citizen

def sumar(a, b):
    return a + b

# 1. Asignar una funcion a una variable

mi_funcion = sumar(5,8)
print(mi_funcion)

# 2. Funcion como argumento y retorno de una funcion dentro de otra

def operacion(a,b,sumar_argumento):
    return sumar_argumento(a,b)

print(f"Resultado: {operacion(3,4,sumar)}")

# 3. Retornar una funcion

def retorno_funcion():
    return sumar

mi_funcion_retornada = retorno_funcion()
print(f"Resultado: {mi_funcion_retornada(15,10)}")