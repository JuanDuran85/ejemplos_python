import json

tabla_datos = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 25,
    "direccion": 'abc',
    "telefono": '123'
}

json_string = json.dumps(tabla_datos)
print(json_string)
print(type (json_string))

datos_nuevos = """
{"abc": "123", "def": "456"}
"""

# para convertir el string en un diccionario
datos_nuevos_diccionario = json.loads(datos_nuevos)
print(datos_nuevos_diccionario)
print(type(datos_nuevos_diccionario))