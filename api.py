import os

import requests
from datetime import datetime

# example post
# resp = post('https://forecast-v2.metoceanapi.com/point/time',
#             headers={'x-api-key': 'BnbUHh3ko1bHaM9bmnXGcm'},
#             json={
#                 "points": [{
#                     "lon": 174.7842,
#                     "lat": -37.7935
#                 }],
#                 "variables": [
#                     "wave.height", ""
#                 ],
#                 "time": {
#                     "from": "2025-08-17T00:00:00Z",
#                     "interval": "3h",
#                     "repeat": 3
#                 }
#             }
#             )
#
# print(resp.json())
# # print just values of wave height:
# print(resp.json()['variables']['wave.height']['data'])

# with open("api_key.txt", "r") as f:
#     api_key = f.read().strip()
api_key = os.environ.get("api_key")

def get_api(spot, interval="1h", repeat=0, model="ww3-gfs.global"):
    resp = requests.post('https://forecast-v2.metoceanapi.com/point/time',
                         headers={'x-api-key': api_key},
                         json={
                             "points": [
                                 spot
                             ],
                             "variables": [
                                 "wave.height",
                                 "wave.height.max",
                                 "wave.height.above-8s",
                                 "wave.period.peak",
                                 "wave.period.above-8s.peak",
                                 "wave.direction.mean",
                                 "wave.direction.peak",
                                 "wave.direction.above-8s.peak",
                             ],
                             "time": {
                                 "from": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
                                 "interval": interval,
                                 "repeat": repeat
                             },
                             # ecwmf not working?
                             "models": [
                                 model
                             ]
                         }
                         )
    data = resp.json()['variables']
    return data

# insurance lady number 099603223
