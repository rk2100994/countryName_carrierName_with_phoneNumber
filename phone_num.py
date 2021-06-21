import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = "" #give your phone number with STD code, For example: India = +91
san_number = phonenumbers.parse(number)

print("GeoLocation",geocoder.description_for_number(san_number, "en"))

service_number = phonenumbers.parse(number)
print("Carrier",carrier.name_for_number(service_number,"en"))
