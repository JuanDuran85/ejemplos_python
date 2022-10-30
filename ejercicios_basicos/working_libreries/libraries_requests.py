"""_summary_

    Working with libraries requests and requests_cache

"""

import requests
import requests_cache

# supported backends: sqlite (default), redis, mongodb, memory. Expires after 10 seconds for example

try:
    requests_cache.install_cache('cache.db',backends='sqlite',expire_after=10)
    response_data: requests.Response = requests.get('https://api.github.com/users/juanduran85')
    print(response_data)
    print(type(response_data))
    result = response_data.json()
    print(result)
    print(response_data.from_cache)  # type: ignore
    for response in result.items():
        print(f"{response}")
except Exception as e:
    print(f"Error en proceso: {e}")