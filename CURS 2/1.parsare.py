
import json

# link = "https://dontpad.com/euro2024"

# Versiunea 1 - citire din fisier + parsare
with open("euro_2024.json") as file_handler:
    # Citire continut
    continut = file_handler.read()
    print(type(continut), continut)
    # Parsez continutul
    continut_parsat = json.loads(continut)
    print(type(continut_parsat), continut_parsat)


# Versiunea 2 - parsare la citire (direct)
with open("euro_2024.json") as file_handler:
    continut_parsat = json.load(file_handler)
    print(type(continut_parsat), continut_parsat)