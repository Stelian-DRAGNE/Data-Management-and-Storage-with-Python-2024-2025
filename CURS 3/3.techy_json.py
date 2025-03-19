
import requests
import json


URL_json = "https://techy-api.vercel.app/api/json"

response = requests.get(URL_json)
print(response)

print(response.status_code)

print(response.content, type(response.content))

print(response.text, type(response.text))

print(response.json(), type(response.json()))

response_json = response.json()
print(response_json["message"])

try:
    with open("techy.json", "r") as file_reader:
        dictionarul_citit = json.load(file_reader)
except:
    dictionarul_citit = {"mesaje":[]}

dictionarul_citit["mesaje"].append(response_json["message"])

with open("techy.json", "w") as file_writer:
    json.dump(dictionarul_citit, file_writer)