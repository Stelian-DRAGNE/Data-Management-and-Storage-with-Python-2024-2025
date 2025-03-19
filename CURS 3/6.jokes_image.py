
import requests
import json
import os


URL = "https://icanhazdadjoke.com/"
headers = {
    "Accept":"application/json"
}
response = requests.get(URL, headers = headers)

print(response.content)

json_dict = response.json()
joke_id = json_dict["id"]

IMAGE_URL = f"https://icanhazdadjoke.com/j/{joke_id}.png"
response = requests.get(IMAGE_URL)
print(response.content)

JOKES_FOLDER = "jokes"

if not os.path.isdir(JOKES_FOLDER):
    os.mkdir(JOKES_FOLDER)

with open(f"{JOKES_FOLDER}/{joke_id}.png", "wb") as fwriter:
    fwriter.write(response.content)