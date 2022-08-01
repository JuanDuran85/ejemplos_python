"""_summary_

 Ejemplo basico de conexion a API y transformando a HTML

"""

import webbrowser
import requests
import string
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY: str = os.getenv("API_KEY")
URL_BASE: str = "https://api.nasa.gov/mars-photos/api/v1"

def get_data_from_api(extra_url: str)-> requests.Response:
    """sumary_line
    
        Keyword arguments:
        argument -- description
        Return: return_description
    
    """
    try:
        response_api: requests.response = requests.get(URL_BASE + extra_url, params={"sol": 1000, "api_key": API_KEY})
        
        if response_api.status_code == 200:
            return response_api
        
        raise requests.RequestException(f"Error al obtener la información: {response_api.status_code}")    
    except Exception as e:
        print(f"Error en API: {e}")
        raise e

def create_html_template(data_from_api: list) -> str:
    """sumary_line
    
        Keyword arguments:
        argument -- description
        Return: return_description
    """
    basic_page_html: string.Template = string.Template("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-A3rJD856KowSb7dwlZdYEkO39Gagi7vIsF0jrRAoQmDKKtQBHUuLZ9AsSv4jD4Xa" crossorigin="anonymous"></script>
    <title>NASA IMG</title>
</head>
<body>
    <div class="container text-center">
        <div class="row">
            ${cards_html}
        </div>
    </div>
</body>
</html>""")
    
    cards = '\n'.join([item for item in data_from_api])
    
    return basic_page_html.substitute(cards_html=cards)
     
result_api: requests.Response = get_data_from_api("/rovers/curiosity/latest_photos")
list_cards_to_html: list = []

for items in result_api.json()["latest_photos"]:
    card_by_item: str = """<div class="col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4 col-xxl-4"><div class="card"><img src="{image}" class="card-img-top" alt="textoi"><div class="card-body"><p class="card-text">{text_description}</p></div></div></div>""".format(image=items['img_src'], text_description=items['earth_date'])
    list_cards_to_html.append(card_by_item)

html_template: str = create_html_template(list_cards_to_html)

with open('output.html', 'w') as file_to_open: 
    file_to_open.write(html_template)
file_to_open.close()

print("Proceso finalizado")

webbrowser.open_new_tab('output.html')