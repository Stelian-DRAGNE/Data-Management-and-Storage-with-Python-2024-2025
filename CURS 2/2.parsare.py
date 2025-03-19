
import json
from pprint import pprint

with open("euro_2024.json") as file_handler:
    continut_parsat = json.load(file_handler)
    # print(type(continut_parsat), continut_parsat)


print(continut_parsat.keys())

tara_cautata = "Romania"

pprint(continut_parsat)

groups = continut_parsat["groups"]
# pprint(type(groups))
# pprint(groups)

for gr in groups:
    print(type(gr))
    pprint(gr["teams"])
    for team in gr["teams"]:
        print(type(team))
        pprint(team)
        if team["name"] == tara_cautata:
            print(f"{tara_cautata} se afla in grupa {gr["name"]}.")
            break