import datetime
from buoydata import get_bouy_data
from api import get_api
import os
import csv

api = get_api({"lon": 173.333, "lat": -43.75})
buoy = get_bouy_data()

if not os.path.isfile("data.csv"):
    with open("data.csv", "w") as csvfile:
        writer = csv.writer(csvfile)
        labels = ["Date and Time", "Local Observations (place)", "Local Observations (wave)"] + list(buoy[0].keys())[1:] + list(api.keys())
        writer.writerow(labels)

with open("data.csv", "a") as csvfile:
    writer = csv.writer(csvfile)
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    data = [now, '', ''] + list(buoy[0].values())[1:] + [val["data"][0] for val in api.values()]
    writer.writerow(data)

