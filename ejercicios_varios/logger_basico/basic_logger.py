import json
from datetime import date, datetime, time
from typing import Any

def json_serial(objeto_in) -> str| None:
    print(type(objeto_in))
    if isinstance(objeto_in, (datetime, date)):
        return objeto_in.strftime('%Y-%m-%d')
    elif isinstance(objeto_in, time):
        return objeto_in.strftime('%H:%M:%S')
    else:
        print("No se puede serializar el objeto: ", objeto_in)
    
def log(body_in: Any) -> None:
    log_body_in: dict = {
        'datetime': datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),
        'body': body_in
    }
    print(json.dumps(log_body_in))
    
    
if __name__ == '__main__':
    log(1)
    print(json_serial(datetime.now()))
