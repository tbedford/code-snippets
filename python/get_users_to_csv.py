import requests

print("email,date_of_birth,status")
while True:

    try:
        response = requests.get("https://random-data-api.com/api/v2/users")
        response_json = response.json()

        email = response_json['email']
        date_of_birth = response_json['date_of_birth']
        status = response_json['subscription']['status']

        print(f"{email},{date_of_birth},{status}")
    except KeyboardInterrupt:
        print('Closing nicely.')
        exit(-1)
