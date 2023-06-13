import csv
from geopy.geocoders import Nominatim
import pandas as pd

def get_geolocation(ip_address):
    geolocator = Nominatim(user_agent="geolocation_example", timeout=3)
    location = geolocator.geocode(ip_address)
#    print(location)
    if location is not None:
        return location.address
    else:
        return "Unknown"

def proc_row(row):
#    print("ip_address: ", row["ip_address"])
    return(get_geolocation(row["ip_address"]))
    
df = pd.read_csv("user_regs.csv")
df["geolocation"] = df.apply(proc_row, axis=1)

print(df)





