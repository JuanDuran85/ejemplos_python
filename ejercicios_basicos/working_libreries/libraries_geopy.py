from geopy.geocoders import Nominatim

def city_location(place_in: str) -> None:
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(place_in)
    print(f"{location = }")

if __name__ == "__main__":
    place: str = input("Enter city name: ")
    city_location(place)