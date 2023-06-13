import csv
from geopy.geocoders import Nominatim


def get_geolocation(ip_address):
    geolocator = Nominatim(user_agent="geolocation_example")
    location = geolocator.geocode(ip_address)
    if location is not None:
        return location.address
    else:
        return "Unknown"

def load_user_registrations(csv_file):
    registrations = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            registrations.append(row)
    return registrations

# Example usage
csv_file = "user_regs.csv"
user_registrations = load_user_registrations(csv_file)
for registration in user_registrations:
    print(registration['ip_address'], ' -- ', get_geolocation(registration['ip_address']))




