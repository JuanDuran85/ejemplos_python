import json, httpx, asyncio, os
from dotenv import load_dotenv

load_dotenv()

headers = {
'Authorization': f"Bearer {os.getenv('BEARER_TOKEN')}"
}
url: str = os.getenv('URL_BASE')

async def main(name_user_in: str):
    try:
        url_final: str = f"{url}users/by?usernames={name_user_in}&user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at"
        async with httpx.AsyncClient() as client:
            response_api: httpx.Response = await client.get(url_final, headers=headers)
            print(response_api)
    except Exception as e:
        print(f"ERROR_API: {str(e)}")
    
async def get_data_from_api(client,url_final):
    try:
        return await client.get(url_final, headers=headers)
    except Exception as e:
        print(f"ERROR: {str(e)}")
    
if __name__ == '__main__':
    name_user: str = input("Ingrese el nombre del usuario a buscar: ")
    asyncio.run(main(name_user))