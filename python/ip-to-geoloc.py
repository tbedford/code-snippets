from geopy.geocoders import Nominatim

def get_geolocation(ip_address):
    geolocator = Nominatim(user_agent="geolocation_example")
    location = geolocator.geocode(ip_address)
    if location is not None:
        return location.address
    else:
        return "Unknown"

# Example usage
ip_address = "192.168.0.1"
geolocation = get_geolocation(ip_address)
print(f"IP: {ip_address} - Geolocation: {geolocation}")
