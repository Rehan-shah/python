import time

import requests
from datetime import datetime
import smtplib as smtp
MY_LAT = 23.022505 # Your latitude
MY_LONG = 72.571365# Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def is_dark():
    return time_now.hour >= sunset and time_now.hour =< sunrise


def is_near():
    return abs(MY_LAT-iss_latitude) <= 5 and abs(MY_LONG-iss_longitude) <= 5


def send_email():
    if is_dark() and is_near() :
        with smtp.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="Rehansnehalshah1@gmail.com" , password='lpcgolzzdttrxgkx')
            connection.sendmail(from_addr='Rehansnehalshah1@gmail.com' ,
                                to_addrs='Rehansnehalshah1@gmail.com' ,
                                msg='Space station is here')
        time.sleep(60)
        send_email()





#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



