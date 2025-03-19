
import requests
import json
from pprint import pprint


URL = "https://api.datamuse.com/words"
lista_parametri = [{"sl":"beautiful"}, {"ml":"women"}]

for parametri in lista_parametri:
    response = requests.get(URL, params = parametri)
    lista_de_dictionare = response.json()

    cuvinte = []
    
    for dictionar in lista_de_dictionare:
        cuvinte.append(dictionar["word"])

    print(cuvinte)