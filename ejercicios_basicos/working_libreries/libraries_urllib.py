"""_summary_

    Using urllib library

"""

from urllib.parse import ParseResult, urlparse
from urllib import request
import json

#----------------------------------------------------------------------------
#
#----------------------------------------------------------------------------

url: str = "https://www.youtube.com/watch?v=PByWVXDTzHw"
parts: ParseResult = urlparse(url)
print(f"{parts = }")
print(f"{parts.scheme = }")
print(f"{parts.netloc = }")
print(f"{parts.path = }")
print(f"{parts.query = }")

#-----------------------------------------------------------------------------
#
#-----------------------------------------------------------------------------

api_url: str = "https://jsonplaceholder.typicode.com/todos/1"
try:
    response_data = request.urlopen(api_url)
    json_response = response_data.read()
    final_data = json.loads(json_response)
    print(f"{final_data = }")
except Exception as e:
    print(e)
    
#-----------------------------------------------------------------------------
#
#-----------------------------------------------------------------------------
print("----------------------------------------------------------------------")
url_two = request.urlopen('https://alirafael.com/')
url_two.geturl()
header_two = url_two.info()
print(header_two.as_string())
print(url_two.getcode())