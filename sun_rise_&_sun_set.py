import requests
from datetime import datetime

MY_LAT = 20.593683
MY_LNG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

# iss_latitude = data["iss_position"]["latitude"]
# iss_longitude = data["iss_position"]["longitude"]

print(data)
sunrise = data["results"]["sunrise"]
print(f"The sunrise time without splitting {sunrise}")
sunrise = data["results"]["sunrise"].split("T")
print(f"The sunrise time after splitting only T {sunrise}")
sunrise = data["results"]["sunrise"].split("T")[1]
print(f"The sunrise time after splitting T selecting the part after T is {sunrise}")
sunrise = data["results"]["sunrise"].split("T")[1].split(":")
print(f"The sunrise time after splitting ':' {sunrise}")

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
print(f"The sunrise time after splitting ':' and if we want particular we index that to 0 which will be {sunrise} hour")


sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()
print(f"Current time is {time_now.hour}:AM")
print(f"sunrises at {sunrise}:AM")
print(f"sunsets at {sunset}:PM")