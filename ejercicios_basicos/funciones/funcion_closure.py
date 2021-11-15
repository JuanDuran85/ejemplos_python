# concepto de closure en python: es una funcion que define a otra y ademas la puede regresar
# la funcion anidada puede acceder a las variables locales definidas en la funcion principal o externa

# funcion principal o externa

def operacion(a,b):
    #definimos una funcion interna o anidada
    def sumar():
        return a + b
    
    # retornar la funcion anidada
    return sumar

mi_funcion_closure = operacion(10,20)
print(mi_funcion_closure())

# llamando la funcion al vuelo
print(operacion(10,20)())

# funcion principal o externa y uso de lambda
def opracion_dos(a,b):
    #definimos una funcion interna o anidada con lambda
    return lambda: a + b

print(opracion_dos(10,20)())