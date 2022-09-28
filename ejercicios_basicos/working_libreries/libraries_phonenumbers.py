import phonenumbers
from phonenumbers import geocoder

try:
    phone_number_in: str = input("Enter the Phone number with +: ")
    phone_number_out: phonenumbers.PhoneNumber = phonenumbers.parse(phone_number_in)
    print(phone_number_out)
    print(f"Location: {geocoder.description_for_number(phone_number_out,'en')}")
except Exception as e:
    print("Error in Phone number")
    raise e