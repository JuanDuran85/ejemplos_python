"""_summary_

  Funciones: 
    - Las funciones en python son ciudadanos de primera clase

    - Primero se definen o importan y luego se usan.
    
    - Las funciones se pueden usar como un objeto, asignando la referencia de la funcion a una varibale sin hacer el llamado a la misma mediante los parentisis
    
    - Cuando se pasa una funcion a otra funcion, se denomina Higher Order Function
"""

# las funciones en python son ciudadanos de primera clase
def mayusculas(texto: str) -> str:
      return texto.upper()
    
# uso normal de las funciones
print(mayusculas("python version 3.10"))

# usando una funcion como objeto
variable_funcion = mayusculas

print(f"Funcion mayusculas {mayusculas}")
print(f"Variable funcion {variable_funcion}")

# para demostrar que las funciones son objetos eliminamos la referencia original mediante la palabra "-del-"
del mayusculas

# ahora se puede utilizar solo la funcion con la variable que apunta a la funcion original
print(f"Funcion mayusculas desde la variable funcion: {variable_funcion('python version 3.10')}")

# si se intenta utilizar la funcion general, se generara un error
try:
    print(f"Funcion mayusculas {mayusculas('Se elimino la referencia')}")
except Exception as e:
    print(f"La funcion no puede ser llamada directamente: {e}")
    
# se puede saber el nombre que se le asigna a una variable al ser referencia de una funcion
print(f"Nombre de la funcion asignada a la variable: {variable_funcion.__name__}")

# --------------------------------------------------------------------------------------------
# Higher Order Function (funciones de alto orden)
# pasando una funcion a otra funcion

def mayusculas_dos(texto: str) -> str:
    return texto.upper()

def saludar(argumento_funcion) -> None:
    # usamos la funcion que recibimos como argumento y devolvemos el resultado al ejecutarla
    referencia_funcion_retornada = argumento_funcion('Nuevo mensaje desde funcion saludar')
    print(f"Funcion saludar: {referencia_funcion_retornada}")
    
# llamamos la funcion saludar pasando la referencia de una funcion como argumento
saludar(mayusculas_dos)

# ejemplo clasico de Higher Order Function con funcion map, la cual, toma una funcion como base y un iterable y luego llama a la funcion con cada elemento proporcionado por el iterable

print(list(map(mayusculas_dos,["nuevo texto","otro texto","ultimo texto de la lista"])))

# -----------------------------------------------------------------------------------------------
# desenpaquetando parametros en funciones

def imprimir_vector(x: int, y: int, z: int) -> str:
    return f"<{x},{y},{z}>"

list_vector: list = [3,5,4]
tupla_vector: tuple = (-1,6,-4)

print(imprimir_vector(*list_vector))
print(imprimir_vector(*tupla_vector))

expresion_vector: list = [x * x for x in range(3)]
print(imprimir_vector(*expresion_vector))

diccionario_vector: dict = {
    'x':3,
    'y':-5,
    'z':-1
}
print(imprimir_vector(**diccionario_vector))
# si se quiere solo pasar las llaves del diccionario
print(imprimir_vector(*diccionario_vector))