
import requests
from bs4 import BeautifulSoup

URL = "https://icanhazdadjoke.com/"
response = requests.get(URL)
parsed_paged = BeautifulSoup(response.content, "html.parser")

# print(parsed_paged, type(parsed_paged))

paragrafe = parsed_paged.find_all("p", {"class":"subtitle"})
# print(paragrafe)

joke = paragrafe[0]
# print(joke)
print(joke.text)