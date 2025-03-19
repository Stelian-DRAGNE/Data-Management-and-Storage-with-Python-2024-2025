
import requests
import json
from pprint import pprint


latitudine = 44.432384
longitudine = 26.1063209

BASE_URL = "https://api.open-meteo.com/"
PATH = "/v1/forecast"

URL = BASE_URL + PATH

parametri = {
    "latitude":latitudine,
    "longitude":longitudine,
    "current":"temperature_2m"
}

response = requests.get(URL, params = parametri)
print(response.request.url)
print(response.status_code)
print(response.content)

json_response = json.loads(response.content)
print(json_response, type(json_response))

temperatura = json_response["current"]["temperature_2m"]
print("Temperatura este:", temperatura)

with open("temperatura_bucuresti", "w") as fwriter:
    fwriter.write(f"{temperatura}")


# curl "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"