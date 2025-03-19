
import requests
import pycountry


URL = "https://api.nationalize.io/"

nume = "Stelian"

response = requests.get(URL, params = {"name":nume})
print(response.request.url)
print(response.status_code)
print(response.json())

response_dict = response.json()
max_country = response_dict['country'][0]["country_id"]


try:
    country_name = pycountry.countries.get(alpha_2=max_country).name
except:
    country_name = "Tara neafiliata."

print(f"Numele {nume} cel mai probabil vine din {country_name}.")