import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
data = (response.json())
print(data)
data = (response.json())["iss_position"]
print(data)
latitude = response.json()["iss_position"]["latitude"]
print(latitude)

longitude = response.json()["iss_position"]["longitude"]
print(longitude)

iss_position = (latitude, longitude)
print(iss_position)
