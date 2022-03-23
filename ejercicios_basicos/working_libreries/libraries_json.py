"""_summary_

    Trabajando con la libreria json de python

"""

import json

tabla_datos = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 25,
    "direccion": 'abc',
    "telefono": '123'
}

# el metodo dumps convierte un diccionario en una cadena de texto json
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

# The json module can print better lines. Thos only work with dicts containing primitive types.
print(json.dumps(tabla_datos, indent=4, sort_keys=True))

# Get all keys and values from json object
with open("/home/juan/Descargas/programacion/ejemplos_python/people.json") as json_file:
    data_file = json.load(json_file)
    print(data_file)
    json_data = data_file["person"]
    for x in json_data:
        keys = x.keys()
        print(keys)
        values = x.values()
        print(values)