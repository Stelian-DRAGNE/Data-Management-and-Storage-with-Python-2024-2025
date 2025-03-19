
import requests


URL_text = "https://techy-api.vercel.app/api/text"

response = requests.get(URL_text)

print(response)

print(response.status_code)

print(response.content, type(response.content))

print(response.text, type(response.text))

try:
    with open("techy.txt", "r") as file_writer:
        contor = len(file_writer.readlines()) + 1
except:
    contor = 1

with open("techy.txt", "a") as file_writer:
    file_writer.write(f"{contor} {response.text}\n")