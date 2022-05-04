"""_summary_

    Concepto de closure en python: es una funcion que define a otra y ademas la puede regresar la funcion anidada puede acceder a las variables locales definidas en la funcion principal o externa.
    
    Las funciones internas pueden capturar y guardar el estado de la funcion externa o padre

"""

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

# -------------------------------------------------------------------------------------------
def hablar(texto: str, volumen: float):
    def minuscula() -> str:
        return texto.lower()
    def mayusculas() -> str:
        return texto.upper()
    if volumen < 0.7:
        return minuscula()
    else:
        return mayusculas()


print(hablar("Texto para LLevar a Minusculas",0.4))
print(hablar("Texto para LLevar a mayusculas",0.9))

# -------------------------------------------------------------------------------------------
def mostrar(titulo: str):
    def saludar(mensaje: str) -> str:
        return f"{titulo} {mensaje}"
    return saludar

mostrar_sr = mostrar("Sr.")
mostrar_sra = mostrar("Sra.")

print(mostrar_sr("Juan"))
print(mostrar_sra("Maria"))

print(callable(mostrar))
