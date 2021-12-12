import json
import urllib.request

respuesta_api = urllib.request.urlopen("http://localhost:3000/data")
cuerpo_respuesta = respuesta_api.read()

json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))

descripcion_clima = json_respuesta['clima'][0]['descripcion']
# se puede hacer tambien de esta manera: descripcion_clima = json_respuesta.get('clima')[0].get('descripcion')

temp_min = json_respuesta['principal']['temp_min']
temp_max = json_respuesta['principal']['temp_max']

print(f"Descripcion del clima: {descripcion_clima}")
print(f"Temperatura minima: {temp_min} °C")
print(f"Temperatura maxima: {temp_max} °C")