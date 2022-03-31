""" ISS OVERHEAD NOTIFIER API FOR A GIVEN LATITUDE AND LONGITUDE """
import time

import requests
import datetime
import smtplib


MY_LAT = 36.7201600
MY_LONG = -4.4203400

def is_iss_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    # print(data)

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # your position is within +5 or -5 degrees of the iss_position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():

    """ Parameters :
            * lat (float): Latitude in decimal degrees. Required.
            * lng (float): Longitude in decimal degrees. Required.
            * date (string): Date in YYYY-MM-DD format. Also accepts other date formats and even relative date formats.
                If not present, date defaults to current date. Optional.
            * callback (string): Callback function name for JSONP response. Optional.
            * formatted (integer): 0 or 1 (1 is default). Time values in response will be expressed following ISO 8601 and
                day_length will be expressed in seconds. Optional."""

    my_parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=my_parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split("+")[0]
    sunset = data["results"]["sunset"].split("T")[1].split("+")[0]
    print(sunrise, sunset)
    time_now = str(datetime.datetime.now()).split()[1].split(".")[0]
    print(time_now)

    if time_now >= sunset or time_now <= sunrise:
        return True

while True:
    time.sleep(100)
    if is_iss_overhead() and is_night():
        my_email = "khashstudioz@gmail.com"
        password = "Hash@123"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()                       # securing our connection
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs= my_email,
                msg=f"Subject:Look Up!\n\nThe ISS is above you in the sky."
            )
