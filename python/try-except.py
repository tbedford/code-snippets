import requests

a = "https://www.example.com:9000/event"
b = "https://tonys-notebook.com"

try:
    r = requests.get(a)
    print(r.status_code)
except Exception as e:
    print("BANG!! ")
    
