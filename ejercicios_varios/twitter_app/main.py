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
            print(response_api.content)
            if response_api.status_code == 200:
                url_user_info: str = f"{url}users?ids={response_api.status_code}&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld&expansions=pinned_tweet_id&tweet.fields=attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,promoted_metrics,public_metrics,referenced_tweets,reply_settings,source,text,withheld"
                info_user: httpx.Response = await client.get(url_user_info, headers=headers)
                print(info_user)
            print(f"El usuario {name_user_in} no existe")
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