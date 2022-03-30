""" SUNRISE AND SUNSET TIME API FOR A GIVEN LATITUDE AND LONGITUDE """

""" Parameters : 
        * lat (float): Latitude in decimal degrees. Required.
        * lng (float): Longitude in decimal degrees. Required.
        * date (string): Date in YYYY-MM-DD format. Also accepts other date formats and even relative date formats. 
            If not present, date defaults to current date. Optional.
        * callback (string): Callback function name for JSONP response. Optional.
        * formatted (integer): 0 or 1 (1 is default). Time values in response will be expressed following ISO 8601 and
            day_length will be expressed in seconds. Optional."""

import requests
import datetime


MY_LAT = 36.7201600
MY_LONG = -4.4203400

my_parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
}
# response = requests.get(url="https://api.sunrise-sunset.org/json", params=my_parameters)
# response.raise_for_status()
# data = response.json()
# print(data)


""" or formatting parameters in url string """
# response = requests.get(url=f"https://api.sunrise-sunset.org/json?lat={MY_LAT}&lng={MY_LONG}")
# response.raise_for_status()
# data = response.json()
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]
# print(sunrise, sunset)


""" formatting sunrise and sunset in 24 hour format """

my_parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LONG,
    "formatted" : 0
}

response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=my_parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise, sunset)
sunrise = sunrise.split("T")[1].split("+")[0]
sunset = sunset.split("T")[1].split("+")[0]
print(sunrise)
print(sunset)
time_now = str(datetime.datetime.now()).split()[1].split(".")[0]
print(time_now)

