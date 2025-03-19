import requests
from pprint import pprint
import random
import time



URL = "https://api.chucknorris.io/jokes/random"
response = requests.get(URL)

with open("chuck_random_jokes.txt", "a") as fwriter:
    fwriter.write(response.json()['value'])
    fwriter.write("\n")



with open("template.html", "r") as freader:
    page_content = freader.read()

print(page_content)

with open("chuck_random_jokes.txt", "r") as freader:
    jokes = freader.readlines()
    print(jokes)


jokes_content = ""
for joke in jokes:
    jokes_content += f"<li> {joke} </li>"

jokes_content = "<ol>" + jokes_content + "</ol>"

page_content = page_content.replace("{{CONTENT}}", jokes_content)
print(page_content)

with open("jokes.html", "w") as fwriter:
    fwriter.write(page_content)