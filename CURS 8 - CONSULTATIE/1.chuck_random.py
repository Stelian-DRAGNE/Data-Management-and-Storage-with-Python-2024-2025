import requests
from pprint import pprint

URL = "https://api.chucknorris.io/jokes/random"
response = requests.get(URL)
print(response.status_code)

print(type(response.content),  response.content)
print(type(response.text), response.text)
print(type(response.json()), response.json())

pprint(response.json())
print(response.json()['value'])

with open("chuck_random_jokes.txt", "a") as fwriter:
    fwriter.write(response.json()['value'])
    fwriter.write("\n")