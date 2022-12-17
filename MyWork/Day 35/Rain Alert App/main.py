import requests

api_key = "PLACEHOLDER"
OWM_Endpoint = "http://api.openweathermap.org/data/2.5/forecast?"

LATITUDE = 39.897671
LONGITUDE = 32.699871

weather_params = {"lat": LATITUDE,
                  "lon": LONGITUDE,
                  "appid": api_key}

response = requests.get(OWM_Endpoint, params=weather_params)

weather_data = response.json()
weather_slice = weather_data["list"][:40]
for three_hourdata in weather_slice:
    condition_code = three_hourdata["weather"][0]['id']

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
# print(weather_data["list"][:40]["weather"])
