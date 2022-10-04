from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

data_manager = DataManager()
flight_sheet = data_manager.get_flight_data()

if flight_sheet[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for line in flight_sheet:
        line["iataCode"] = flight_search.get_iataCode(line["city"])
        data_manager.flight_data = flight_sheet
    data_manager.put_iatacode()
else:
    flight_data = FlightData()
    flight_data.find_lowest(data_manager.flight_data)
    user = NotificationManager()
    if user.state:
        data_manager.post_users(f_name=user.first_name, l_name=user.last_name, email=user.first_email)


