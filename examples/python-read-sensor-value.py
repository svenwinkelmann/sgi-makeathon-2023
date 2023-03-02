import requests
from http import HTTPStatus

# how we can get values
response = requests.get("http://127.0.0.1:5000/all")
if response.status_code == HTTPStatus.OK:
    temp_sensor1 = response.json()['temp']['1']
    print(f"Our sensor 1 has the value {temp_sensor1}\n")
else:
    print("Request error")

# control some actions

response = requests.post("http://127.0.0.1:5000/move/plant1")
if response.status_code == HTTPStatus.OK:
    print(f"{response.text}\n")
else:
    print("Request error")

# change simon 2
# change dominik 2