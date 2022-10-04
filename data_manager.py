import requests

API_END = "your api"
API_END_USERS = "your api"


class DataManager:

    def __init__(self):
        self.flight_data = {}

    def get_flight_data(self):
        response = requests.get(API_END)
        self.flight_data = response.json()["prices"]
        return self.flight_data

    def put_iatacode(self):
        for line in self.flight_data:
            params = {
                "price": {
                    "iataCode": line["iataCode"]
                }
            }
            requests.put(url=f"{API_END}/{line['id']}", json=params)

    def post_users(self, f_name, l_name, email):
        params = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email
            }
        }
        requests.post(url=f"{API_END_USERS}", json=params)
