'''
Geopy Library
    Geopy makes it easy for Python developers to locate the coordinates of addresses, cities, countries, and landmarks across the globe using third-party geocoders and other data sources.

'''

from geopy.geocoders import Nominatim
from geopy.adapters import AioHTTPAdapter
import asyncio

class GeopyLibrary:
    @staticmethod
    def geolocator_conexion():
        return Nominatim(user_agent="geoapiExercises")
    
    @staticmethod
    def get_location(geolocator: Nominatim, value_in: str):
        return geolocator.geocode(value_in)
    
async def address_location(addres: str)-> None:
    async with Nominatim(user_agent="geoapiExercises", adapter_factory=AioHTTPAdapter,) as geolocator:
        location: str = await geolocator.geocode(addres) or "No existe"  # type: ignore
        print(f"{location.address = }")# type: ignore

def get_city_location(place_in: str) -> None:
    geolocator = GeopyLibrary.geolocator_conexion()
    location = GeopyLibrary.get_location(geolocator,place_in)
    print(f"{location = }")
    
def get_address_by_zipcode(zip_code: str)-> None:
    geolocator = GeopyLibrary.geolocator_conexion()
    location_by_zipcode = GeopyLibrary.get_location(geolocator,zip_code)
    print(f"{location_by_zipcode = }")

if __name__ == "__main__":
    place: str = input("Enter city name: ")
    get_city_location(place)
    asyncio.run(address_location(place))
    zipcode: str = input("Enter the zipcode: ")
    get_address_by_zipcode(zipcode)