'''
Extract text from any website (URL) 
'''

import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key: str = os.getenv("API_KEY_TWO") or ''
url_base: str = os.getenv("URL_BASE_TWO") or ''

headers = {
    "api-key": api_key,
    "content-type": "application/json",
    "accept": "application/json",
}

payload = {
    "input":"https://alirafael.com/",
    "input_type": "auto-detect",
    "encoding": "utf8",
    "steps": [
       { "skill":"html-extract-article"}
    ]
}

response = requests.post(url_base,json=payload,headers=headers)
result = response.json()
print(result)