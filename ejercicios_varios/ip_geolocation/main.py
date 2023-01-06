import httpx, json, asyncio, os
from dotenv import load_dotenv

load_dotenv()

async def get_ip_location(ip_to_find:str):
    try:
        url_base: str | None = os.getenv("URL")
        api_key: str | None = os.getenv("API_KEY")
        ip_address: str = f"ip_address={ip_to_find if len(ip_to_find)>1 else ''}"
        async with httpx.AsyncClient() as client:
            response_api: httpx.Response = await client.get(f"{url_base}?api_key={api_key}&{ip_address}")
            print(response_api.text)
    except Exception as e:
        print(f"ERROR_GET_DATA: {str(e)}")
    
if __name__ =='__main__':
    ip_to_find: str = ""
    asyncio.run(get_ip_location(ip_to_find))