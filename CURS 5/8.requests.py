
import requests
from bs4 import BeautifulSoup


URL = "http://127.0.0.1:5500/7.index.html"

response = requests.get(URL)
print(response.status_code)
# print(response.text)

parsed_page = BeautifulSoup(response.text, "html.parser")
# print(parsed_page)
elem = parsed_page.find("p")
print(elem)

all_elements = parsed_page.find_all("p")
print(all_elements)