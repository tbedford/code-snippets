import requests

while True:
    response = requests.get("https://random-data-api.com/api/v2/users")
    user = response.json()
    print(f"{user['email']},{user['date_of_birth']},{user['subscription']['status']}")

