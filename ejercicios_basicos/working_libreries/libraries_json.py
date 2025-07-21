# !/usr/bin/python3
# flake8: noqa: E501
# pylint: disable=line-too-long
# pylint: disable=C0103

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
print(type(json_string))

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

# Creating a json file


def create_json_file(path: str, obj: dict) -> None:
    with open(path, 'w') as json_file:
        json.dump(obj, json_file)


if __name__ == '__main__':
    object_to_file: dict = {
        "menu": {
            "id": "file",
            "value": "File",
            "popup": {
                "menuitem": [
                    {"value": "New", "onclick": "CreateNewDoc()"},
                    {"value": "Open", "onclick": "OpenDoc()"},
                    {"value": "Close", "onclick": "CloseDoc()"}
                ]
            }
        }
    }
    create_json_file('test.json', object_to_file)
