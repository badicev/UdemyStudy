# An application programming interface (API) is a set of commands, functions, protocols, and objects that programmers
# can use to create software or *interact with an external system.*


import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)

''' 
1XX: Hold On
2XX: Here You Go
3XX: Go Away
4XX: You Screwed Up
5XX: I Screwed Up
'''

print(response.status_code)

# if response.status_code != 200:
#     print("Bad response from ISS API")

if response.status_code == 404:
    raise Exception("That resource doesn't exist.")
elif response.status_code == 401:
    raise Exception("You are not authorised to access this data.")


data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(iss_position)

