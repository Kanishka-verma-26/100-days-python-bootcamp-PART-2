import requests

response = requests.get(url="http://open-notify.org/Open-Notify-API/ISS-Location-Now/")
print(response)

""" we didn't see any JSON data here but we can see 200 i.r. our response code """