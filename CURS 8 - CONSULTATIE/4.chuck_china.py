import requests
from pprint import pprint
import random

URL = "https://api.chucknorris.io/jokes/search"

params = {
    "query":"china"
}
response = requests.get(URL, params=params)
print(response.request.url)
print(type(response.json()))
print(type(response.json()['result']))

total = response.json()['total']
random_joke_index = random.randint(0, total-1)
print("Gluma de la indexul:", random_joke_index)
print(response.json()['result'][random_joke_index]['value']) 