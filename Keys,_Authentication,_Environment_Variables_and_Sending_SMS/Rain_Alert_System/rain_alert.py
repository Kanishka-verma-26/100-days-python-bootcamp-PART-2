""" This project will check the weather forecast of next 12 hours and send you a message at every 7 am that
 whether you should carry your umbrella to your work or not """

""" sending sms """
import os
from twilio.rest import Client
import requests

api_key = "c255a84019eba778cdde4c13119b68d6"
account_sid = "AC0c7ee8fc151cee3407dcfae02ebcf0e7"
auth_token = "8b9c5946c8d61514eaa3eeca75d73de3"

weather_params = {
    "lat": 28.704060,
    "lon": 77.102493,
    "appid" : api_key,
    "exclude": "current,minutely,daily",
}

""" The below API contains currently, minutely, hourly and daily weather report """
""" but we only want the hourly weather report so we will exculde the unwanted data, 
    this will speed up the fetching process and it should be comma-delimited list (without spaces) """

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)


""" the hourly data representation :
        "hourly": [
        {
          "dt": 1618315200,
          "temp": 282.58,
          "feels_like": 280.4,
          "pressure": 1019,
          "humidity": 68,
          "dew_point": 276.98,
          "uvi": 1.4,
          "clouds": 19,
          "visibility": 306,
          "wind_speed": 4.12,
          "wind_deg": 296,
          "wind_gust": 7.33,
          "weather": [
            {
              "id": 801,                        # # weather condition id
              "main": "Clouds",
              "description": "few clouds",
              "icon": "02d"
            }
          ],
          "pop": 0
          },
        ]
        
        
        
*** The Weather Conditions ***
    
    refer: "https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2"
    
    Group 2xx: Thunderstrom
    Group 3xx: Drizzle
    Group 5xx: Rain
    Group 6xx: Snow
    Group 7xx: Atmosphere
    Group 800: Clear
    Group 80x: Clouds
    
Note : we are gonna provide a message for id < 700

"""


""" checking the need of umbrella for next 12 hours """
will_rain = False

for i in range(12):
    condition_code = weather_data["hourly"][i]["weather"][0]["id"]              # return id
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Don't forget to carry an umbrella ☂️.",
        from_='+15716006490',
        to='+918800868544'
    )

    print(message.status)






