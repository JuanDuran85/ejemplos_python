'''
Geopy Library
    Geopy makes it easy for Python developers to locate the coordinates of addresses, cities, countries, and landmarks across the globe using third-party geocoders and other data sources.

'''

from geopy.geocoders import Nominatim
from geopy.adapters import AioHTTPAdapter
import asyncio

async def address_location(addres: str):
    async with Nominatim(user_agent="geoapiExercises", adapter_factory=AioHTTPAdapter,) as geolocator:
        location: str = await geolocator.geocode(addres) or "No existe"  # type: ignore
        print(location.address)# type: ignore

def city_location(place_in: str) -> None:
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(place_in)
    print(f"{location = }")

if __name__ == "__main__":
    place: str = input("Enter city name: ")
    city_location(place)
    asyncio.run(address_location("Maule 150"))
    