import requests
from pprint import pprint


URL = "https://api.chucknorris.io/jokes/random"

params = {
    "category":"political"
}
response = requests.get(URL, params=params)
print(response.request.url)


print(type(response.json()))
print(response.json()['value'])