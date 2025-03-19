
import requests
import random
import json
import time


api_options = ["", "-gcp", "1", "2", "3", "4"]
valoare = random.choice(api_options)
BASE_URL = f"https://api{valoare}.binance.com"
print(BASE_URL)

PATH = "/api/v3/avgPrice"

URL = BASE_URL + PATH
print(URL)

symbol = "ETHUSDT"

def call_api():
    response = requests.get(URL, params = {"symbol":symbol})
    print(response.status_code)
    print(response.content, type(response.content))

    # Deserializare
    json_response = json.loads(response.content)
    print(json_response, type(json_response))

    price = json_response['price']
    print("price =", price)

    with open("ethereum.txt", "a", encoding = "utf-8") as fwriter:
        fwriter.write(price)
        fwriter.write("\n")

if __name__ == "__main__":
    while True:
        call_api()
        cat_doarme = random.randint(1, 3)
        print("Doarme ...", cat_doarme, "secunde.")
        time.sleep(cat_doarme)