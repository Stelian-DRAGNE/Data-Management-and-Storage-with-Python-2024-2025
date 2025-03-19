
import requests
from pprint import pprint


URL = "https://catfact.ninja/fact"
for i in range(3):
    fact = requests.get(URL).json()['fact']
    print(fact)
    with open("cat_facts.txt", "a") as fwriter:
        fwriter.write(fact + "\n")