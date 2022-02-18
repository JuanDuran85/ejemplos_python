"""" 
Patrones estructurales: Adapter

Este patrón "proporciona una interfaz unificada a un conjunto de interfaces en un subsistema"

Un adaptador se puede considerar como la aplicación del principio de inversión de dependencias (DIP), cuando la clase de alto nivel define su propia interfaz (adaptador) para el módulo de bajo nivel (implementado por una clase adaptada).

El patron adaptador actua como un conector entre dos interfaces que son incompatibles y que no pueden estar conectadas directamente.

"""

from abc import ABC, abstractmethod

class Adapter(ABC):
    
    @abstractmethod
    def converter(self, object): ...

# las clases heredan de la clase adapter    
class ToJson(Adapter):
    
    def converter(self, object)-> dict:
        return conver_to_json(object)  
    
class FromJson(Adapter):
    
    def converter(self, object):
        return conver_to_object(object)
    
class Object: ...

# se recibe un objeto(clase) de python y se lleva a json
def conver_to_json(python_object)-> dict:
    json_object = {}
    for key, value in python_object.__dict__.items():
        json_object[key] = value
    return json_object

# se recibe un json para pasar a objeto "clase" en python
def conver_to_object(json: dict)-> Object:
    object_python = Object()
    for key,value in json.items():
        object_python.__setattr__(key, value)
    return object_python

object_one = Object()
object_one.name = "Juan"
object_one.age = 23
object_one.email = "email@email.com"

conver_json = ToJson()
result = conver_json.converter(object_one)
print(result)

json_one = {
    "city": "Bogota",
    "country": "Colombia",
    "population": "1.5 millones"
}

conver_object = FromJson()
result = conver_object.converter(json_one)
print(result)
for key,value in result.__dict__.items():
    print(f"{key}: {value}")

