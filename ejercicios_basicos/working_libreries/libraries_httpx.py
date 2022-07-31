"""_summary_

    Working with library httpx.
    
    HTTPX is a fully featured HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.
    
    pip install httpx

"""

import httpx
import asyncio

print("\n-------------------using async client----------------------\n")
# using async client

url_base_api_async: str = "https://mindicador.cl/api"

async def get_data_api_async() -> None:
    """_summary_

    Raises:
        e: _description_
    """
    try:
        async with httpx.AsyncClient() as client:
            response_api_async: httpx.Response = await client.get(url_base_api_async)
            print(response_api_async)
            print(response_api_async.json())
            print(response_api_async.status_code)
            print(response_api_async.text)
            print(response_api_async.headers)    
    except Exception as e:
        print(f"Error: {e}")
        raise e

asyncio.run(get_data_api_async())

print("\n-------------------using top level api-----------------------\n")
# using top level api

url_base_api: str = "https://api.victorsanmartin.com/feriados/en.json"

try:
    response_api: httpx.Response = httpx.get(url_base_api)
except Exception as e:
    print(f"Error: {e}")
    raise e

print(response_api)
print(response_api.json())
print(response_api.status_code)
print(response_api.text)
print(response_api.headers)

print("\n-------------------using client-----------------------\n")
# using client

url_base_api_client: str = "https://jsonplaceholder.typicode.com/users"
with httpx.Client() as client:
    repsonse_api_client: httpx.Response = client.get(url_base_api_client)
    print(repsonse_api_client.json())



