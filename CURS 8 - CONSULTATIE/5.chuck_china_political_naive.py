import requests
from pprint import pprint
import time

URL = "https://api.chucknorris.io/jokes/random"

params = {
    "category":"political"
}

a_gasit = False

while not a_gasit:
    response = requests.get(URL, params=params)
    gluma = response.json()['value']
    a_gasit = "china" in gluma.lower()
    print(gluma)
    time.sleep(6)