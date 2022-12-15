# An application programming interface (API) is a set of commands, functions, protocols, and objects that programmers
# can use to create software or *interact with an external system.*
MY_LATITUDE = 39.933365
MY_LONGITUDE = 32.859741
MY_EMAIL = "basakdilaracevik4@gmail.com"
MY_PASSWORD = "MyPassword1234"

import requests
from datetime import datetime
import smtplib
import time

''' 
1XX: Hold On
2XX: Here You Go
3XX: Go Away
4XX: You Screwed Up
5XX: I Screwed Up
 '''


# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response.status_code)
#
# if response.status_code != 200:
#     print("Bad response from ISS API")
#
# if response.status_code == 404:
#     raise Exception("That resource doesn't exist.")
# elif response.status_code == 401:
#     raise Exception("You are not authorised to access this data.")
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    data = response.json()
    # print(data)

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # iss_position = (longitude, latitude)

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5:
        return True


# print(iss_position)
def is_night():
    parameters = {"lat": MY_LATITUDE,
                  "lng": MY_LONGITUDE,
                  "formatted": 0}

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="cevikbasakdilara@gmail.com",
            msg="Subject:Look Up \n\nThe ISS is above you in the sky."
        )

# If the ISS is close to my current position,
# and it is currently dark
# Then email me to tell me to look up.
# BONUS: Run the code every 60 seconds.
