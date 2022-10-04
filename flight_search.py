import requests

KIWI_END = "your api"
KIWI_APIKEY = "your api"


class FlightSearch:

    def get_iataCode(self, city_name):
        header = {
            "apikey": KIWI_APIKEY
        }
        params = {
            "term": city_name
        }
        response = requests.get(url=f"{KIWI_END}/locations/query", params=params, headers=header)
        kiwi_data = response.json()["locations"][0]["code"]
        return kiwi_data
