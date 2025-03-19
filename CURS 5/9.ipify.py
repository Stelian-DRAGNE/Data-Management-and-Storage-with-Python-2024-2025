
import requests
from bs4 import BeautifulSoup

URL = "https://api.ipify.org/"
response = requests.get(URL)
parsed_paged = BeautifulSoup(response.content, "html.parser")

print(parsed_paged, type(parsed_paged))