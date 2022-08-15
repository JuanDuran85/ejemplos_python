#        Desafío - Website Pájaros

"""
Elaborado por Elio Duran

Requerimientos:

1. Crear templates del HTML a utilizar.

2. Generar un llamado a la API que permita recopilar la 
información necesaria para construir el sitio.

3. Exportar el sitio creado como un archivo html que pueda
ser abierto en el navegador.

Nota adicional: el sitio web a crear debe generar un listado
con las Aves de Chile, y cada especie registrada con
su nombre en inglés y español junto con sus imágenes.
"""
import requests
import json
from string import Template

# Se trae la información de la API dispoble desde el site: "https://aves.ninjas.cl/"
url = "https://aves.ninjas.cl/api/birds"

"""PARTE 1: Crear template del HTML a utilizar"""  
def templates_html():
    template = Template("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Elio_Duran</title> <!--Titulo de la pagiina-->
    </head>
    <body>
        <h1>        ****    AVES CHILENAS    ***</h1> 
        <ul>
            ${lista_url}
        </ul>
    </body> 
    </html>
    """)
    return template

"""PARTE 2: Llamar a la API para recopilar la inf. para construir el sitio."""
def request(url):
    response = requests.request("GET",url)
    if response.status_code == 200: #Validadando que la respuesta del site sea correcto.
        content = response.content
        print(f'\n *** Bienvenidos: Consulta Exitosa a la API-{url} \n')
        return json.loads(content) # Se convierte en un diccionario
    return print('\n !!!!... Consulta errónea \n')

aves_api = request(url) # Se invoca la función request() y se guarda el
                        #resultado en una variable
#n=int(input(('-->Ingrese la cantidad (entre 1 al 216) de fotos que desea ver: ')))

"""PARTE 3: Exportar archivo html"""
# Creación y filtrado de listas fotos desde el diccionario principal de la API

def web_aves_chile(): #generación de la función web_aves_chile()
    """Crear la pagina web con las fotos"""
    name,spanish,english,lista_url,images=[],[],[],[],[]
    for i in range(len(aves_api)): 
        name.append(aves_api[i]['name']) # Se crea una lista con los nombres de las especies
        spanish.append(name[i]['spanish']) #lista para guardar el nombre en español
        english.append(name[i]['english']) #lista para guardar el nombre en inglés
        images.append(aves_api[i]['images']) #lista de los indices las fotos
        lista_url.append(images[i]['main']) #lista para guardar las url de las fotos

    # Se crea la lista de las fotos con sus repectivos nobres en español y en inglés.
    lista_url= '\n'.join(['<li>Nombre: ' + spanish[index] + ' / Name: ' + english[index] + '<img src="' + item+ '"></li>' for index, item in enumerate(lista_url)])

    template = templates_html() # Se invoca la función templates_html() para crear la palntilla
    page = template.substitute(lista_url=lista_url) # Se sustituye el template con la lista de
                                                    #fotos
    return page

html = web_aves_chile() # Llamado a la función web_aves_chile() y guardado el resultado

with open('output.html', 'w') as f: # Se crea y se llena el archivo html para abrir en el navegador
    f.write(html)
f.close()



