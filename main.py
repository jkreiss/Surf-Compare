from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from buoydata import get_bouy_data
from api import get_api

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory="templates")

SPOTS = {
    "lebons": {"lon": 173.333, "lat": -43.75},
    "kaikoura": {"lon": 173.682, "lat": -42.4},
    "hurunui": {"lon": 173.173, "lat": -42.542},
    "newbrighton": {"lon": 172.75, "lat": -43.52},
    "rakaia": {"lon": 172.224, "lat": -43.900},
}
gfsdata = {spot: get_api(coords) for spot, coords in SPOTS.items()}
ecmwfdata = {spot: get_api(coords, model="ww3-ecmwf.global") for spot, coords in SPOTS.items()}

@app.get("/buoy")
def get_buoy():
    buoy = get_bouy_data()
    # print(buoy)
    return buoy
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "spots": list(SPOTS.keys())}
    )

@app.get("/forecast/gfs/{spot}")
def get_gfs_forecast(spot: str):
    return {"spot": spot, "forecast": gfsdata[spot]}

@app.get("/forecast/ecmwf/{spot}")
def get_ecwmf_forecast(spot: str):
    return {"spot": spot, "forecast": ecmwfdata[spot]}


