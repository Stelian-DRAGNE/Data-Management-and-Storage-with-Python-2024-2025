
import requests
from pprint import pprint


URL = "https://randomuser.me/api"

response = requests.get(URL)
response_dict = response.json()
pprint(response_dict["results"][0]["name"])

user_dict = response_dict["results"][0]["name"]
print(user_dict["title"], user_dict["first"], user_dict["last"])