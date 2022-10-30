'''
Using http library with requests for good implementations

# http is a package that collects several modules for working with the HyperText Transfer Protocol

'''

from http import HTTPStatus
import requests

# the correct way to use http with requests

response: requests.Response = requests.get("https://alirafael.com/")
if response.status_code == HTTPStatus.OK:
    print(response)
    print("Everything is fine")
