# Leer el archivo

import urllib.request
import json

respuesta = urllib.request.urlopen('http://localhost:3000/data')
print(respuesta)
cuerpo = respuesta.read()
json_respuesta = json.loads(cuerpo.decode('utf-8'))
print(json_respuesta)
# imprimir solo nombres de las personas, se convierte a listas o diccionarios en python
for persona in json_respuesta['personas']:
    print(persona['nombre'], persona['edad'])

datos = {}
for elementos in json_respuesta['data_global']:
    print(elementos)
    datos.update(elementos)

print(datos['total'])
print(datos['mensaje'])
