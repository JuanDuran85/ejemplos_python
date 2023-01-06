from dotenv import load_dotenv
import httpx
import asyncio
import os

load_dotenv()

async def main(text_in: str):
    api_key: str | None = os.getenv('API_KEY')
    url_base: str | None = os.getenv('URL')
    try:
        async with httpx.AsyncClient() as client:
            url_final: str = f"{url_base}?key={api_key}&h1=en-us&v=Amy&src={text_in}"
            response_api: httpx.Response = await client.get(url_final)
            print(response_api)
            with open("audio.mp3","wb") as file:
                file.write(response_api.content)
            
    except Exception as e:
        print(f"ERROR_API: {str(e)}")
        raise e
    
if __name__ =="__main__":
    text_in_user: str = input("Ingrese el texto a transformar a voz: ")
    asyncio.run(main(text_in_user))
    