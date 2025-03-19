
import requests
import json


zip_code = 90210
country = "US"

zip_code = "e62bt"
country = "GB"

zip_code = "79015"
country = "US"

zip_code = "10045"
country = "US"

URL = f"https://api.zippopotam.us/{country}/{zip_code}"
response = requests.get(URL)

print(response.status_code)
print(response.content)

json_response = json.loads(response.content)
print(type(json_response), json_response)