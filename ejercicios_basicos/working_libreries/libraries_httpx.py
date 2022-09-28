"""_summary_

    Working with library httpx.
    
    HTTPX is a fully featured HTTP client for Python 3, which provides sync and async APIs, and support for both HTTP/1.1 and HTTP/2.
    
    pip install httpx

"""

import httpx
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

print("\n-------------------using async client----------------------\n")
# using async client
async def get_data_api_async() -> None:
    """_summary_

    Raises:
        e: _description_
    """
    url_base_api_async: str = "https://mindicador.cl/api"
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
print("\n-----------------------------------------------------------\n")

print("\n-------------------using top level api-----------------------\n")
# using top level api
def ejemplo_top_level():
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
print("\n----------------------------------------------------------\n")

print("\n-------------------using client-----------------------\n")
# using client
def using_client_basic():
    url_base_api_client: str = "https://jsonplaceholder.typicode.com/users"
    with httpx.Client() as client:
        repsonse_api_client: httpx.Response = client.get(url_base_api_client)
        print(repsonse_api_client.json())
print("\n--------------------------------------------------------\n")

print("\n-------------------using async client and task-----------------------\n")
# using client and task
async def weather_async(values_in):    
    try:
        url_base: str = os.getenv("URL_BASE_WA")
        api_key: str = os.getenv("API_KEY_WA")
        async with httpx.AsyncClient() as client:
            task_to_do: list = []
            for index,value in enumerate(values_in):
                print(index,value)
                url_final:str = f"{url_base}?key={api_key}&q={value}&aqi=yes"
                task_to_do.append(asyncio.create_task(send_info_to_api(client, url_final)))
            result_final: list = await asyncio.gather(*task_to_do)
            print(result_final)
    except Exception as e:
        print(f"ERROR_READ_DATA: {e}")
        raise e
async def send_info_to_api(client, url_final: str):
    try:
        response = await client.get(url_final)
        return response.json()
    except Exception as e:
        print(f"ERROR_GET_DATA: {str(e)}")
        raise e
print("\n--------------------------------------------------------\n")

if __name__ == '__main__':
    locations: list[str] = ["Chile","Venezuela","Argentina","Brazil","Canada"]
    asyncio.run(weather_async(locations))
    asyncio.run(get_data_api_async())
    ejemplo_top_level()
    using_client_basic()