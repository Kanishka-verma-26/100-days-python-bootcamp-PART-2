import requests

# response = requests.get(url="http://open-notify.org/Open-Notify-API/ISS-Location-Now/")
# if response.status_code == 404:
#     raise Exception("That resource doesn't exist.")
# elif response.status_code != 401:
#     raise Exception("You are not authorised to access this data.")

""" Note: there are a lot of status codes that you could be getting back 'https://www.webfx.com/web-development/glossary/http-status-codes/' 
     and its impossible to write this many if statements checking for single possibility instead we can use the request
    module to generate the exception instead such as 'response.raise_for_status()' will raise an HTTPError if the HTTP
     request returned an unsuccessful status code.
    
    The request module is the most popular way for python developers to work with APIs"""

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = data['iss_position']['longitude']
latitude = data['iss_position']['latitude']
is_position = (longitude, latitude)
print(is_position)



