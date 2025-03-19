import requests
from pprint import pprint
import random

URL = "https://api.chucknorris.io/jokes/search"

params = {
    "query":"china"
}
response = requests.get(URL, params=params)
# pprint(response.json()['result'])


joke_list = response.json()['result']
for joke_dict in joke_list:
    if 'political' in joke_dict['categories']:
        print(joke_dict['value'])