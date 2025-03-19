
import requests


URL = "https://api.dicebear.com/9.x/lorelei/svg"
response = requests.get(URL)
print(response.text)

# V1 - scriere string
with open("lorelei.svg", "w") as fwriter:
    fwriter.write(response.text)

# V2 - scriere binara
with open("lorelei.svg", "wb") as fwriter:
    fwriter.write(response.content)