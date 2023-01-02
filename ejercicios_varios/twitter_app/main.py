import json, httpx, asyncio, os
from dotenv import load_dotenv

load_dotenv()

headers = {
'Authorization': f"Bearer {os.getenv('BEARER_TOKEN')}"
}
url: str = os.getenv('URL_BASE') or ""

async def main(name_user_in: str):
    try:
        url_final: str = f"{url}users/by?usernames={name_user_in}&user.fields=created_at&expansions=pinned_tweet_id&tweet.fields=author_id,created_at"
        async with httpx.AsyncClient() as client:
            response_api: httpx.Response = await get_data_from_api(client, url_final) # type: ignore
            if response_api.status_code == 200:        
                result_json = response_api.json()
                print(json.dumps(result_json, indent=4, sort_keys=True))
                return result_json
            return None
    except Exception as e:
        print(f"ERROR_API: {str(e)}")


async def get_follow_users(id_user_in: str,mode_find):
    try:
        url_final: str = f"{url}users/{id_user_in}/{mode_find}"
        async with httpx.AsyncClient() as client:
            response_api: httpx.Response = await get_data_from_api(client, url_final) # type: ignore            
            result_json = response_api.json()
            print(json.dumps(result_json, indent=4, sort_keys=True))
            return result_json
    except Exception as e:
        print(f"ERROR_API: {str(e)}")
        
async def get_data_from_api(client,url_final: str):
    try:
        return await client.get(url_final, headers=headers)
    except Exception as e:
        print(f"ERROR: {str(e)}")
    
if __name__ == '__main__':
    name_user: str = input("Ingrese el nombre del usuario a buscar: ")
    info_user = asyncio.run(main(name_user))
    
    if not info_user.get("errors") : # type: ignore
        id_user: str = info_user["data"][0]["id"] # type: ignore
        followers = asyncio.run(get_follow_users(id_user,"followers"))
        following = asyncio.run(get_follow_users(id_user,"following"))
    else:
        print("El usuario no existe")
                    
            # url_user_info: str = f"{url}users?ids={id_user}&user.fields=created_at,description,entities,id,location,name,pinned_tweet_id,profile_image_url,protected,public_metrics,url,username,verified,withheld&expansions=pinned_tweet_id&tweet.fields=attachments,author_id,context_annotations,conversation_id,created_at,entities,geo,id,in_reply_to_user_id,lang,non_public_metrics,organic_metrics,possibly_sensitive,promoted_metrics,public_metrics,referenced_tweets,reply_settings,source,text,withheld"
