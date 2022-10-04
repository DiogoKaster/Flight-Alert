import requests
import datetime as dt
import smtplib
from dateutil.relativedelta import relativedelta

API_KEY = "your key"
API_END = "your api"
API_END_USERS = "your api"


class FlightData:

    def __init__(self):
        self.low_prices = []

    def find_lowest(self, sheet_data):
        today = dt.datetime.now().strftime("%d/%m/%Y")
        six_months = dt.datetime.now() + relativedelta(months=+6)
        six_months = six_months.strftime("%d/%m/%Y")
        print(six_months)
        for line in sheet_data:
            destination = line["iataCode"]
            header = {
                "apikey": API_KEY
            }
            params = {
                "fly_from": "BR",
                "fly_to": destination,
                "date_from": today,
                "date_to": six_months
            }

            response = requests.get(url=API_END, params=params, headers=header)
            search_data = response.json()
            if search_data["data"][0]["price"] < line["lowestPrice"]:
                low_dict = {
                    "City From": search_data["data"][0]["cityCodeFrom"],
                    "City To": search_data["data"][0]["cityCodeTo"],
                    "Price": search_data["data"][0]["price"],
                    "Departure Date": search_data["data"][0]["route"][0]["local_departure"][:10]
                }
                self.low_prices.append(low_dict)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="your email", password="your password")
            response = requests.get(url=API_END_USERS)
            user_emails = response.json()["users"][0]["email"]
            for email in user_emails:
                for low in self.low_prices:
                    connection.sendmail(
                        from_addr="your email",
                        to_addrs=f"{email}",
                        msg=f"Subject:Low price to go to {low['City To']}\n\nIt is currently {low['Price']}")
