import requests
from pprint import pprint

URL = "https://api.chucknorris.io/jokes/categories"
response = requests.get(URL)

print(response.json(), type(response.json()))