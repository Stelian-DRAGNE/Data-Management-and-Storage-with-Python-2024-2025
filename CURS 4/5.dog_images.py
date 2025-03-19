
import requests
from pprint import pprint
import os
import uuid


URL = "https://dog.ceo/api/breeds/image/random"
response = requests.get(URL)
print(response.json())

SECOND_URL = response.json()["message"]
response = requests.get(SECOND_URL)
print(response.content)

try:
    os.mkdir("DOGS")
except:
    pass

filename = "DOGS/" + SECOND_URL.split("/")[-1]
with open(filename, "wb") as fwriter:
    fwriter.write(response.content)

random_name = str(uuid.uuid4()).split("-")[0]
print(random_name)
file_name = "DOGS/" + random_name + "jpg"
with open(filename, "wb") as fwriter:
    fwriter.write(response.content)