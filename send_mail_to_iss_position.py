import time
import requests
from datetime import datetime
import smtplib

MY_EMAIL = "karanth.savi3@gmail.com"
MY_PASSWORD = "cjlh gotg lcgt lxfd"

MY_LAT = 32.735592
MY_LNG = -97.107109


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)
    iss_position = data["iss_position"]
    print(iss_position)

    iss_longitude = data["iss_position"]["longitude"]
    print(iss_longitude)
    iss_latitude = data["iss_position"]["latitude"]
    print(iss_latitude)
    print()

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)

    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

    print(sunrise)
    print(sunset)

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="vasudevarao.karanth@gmail.com",
                        msg="Subject:\n\nLook up")
