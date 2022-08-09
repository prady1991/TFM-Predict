from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import pytz
import pandas as pd
import joblib

app = FastAPI()

app.add_middleware(CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.get("/")
def index():
    return {"greeting": "Hello world"}


@app.get("/predict")
def predict(pickup_datetime,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude,passenger_count):
    
    pickup_datetime = datetime.strptime(pickup_datetime, "%Y-%m-%d %H:%M:%S")
    eastern = pytz.timezone("US/Eastern")
    utc_pickup_datetime= eastern.localize(pickup_datetime, is_dst=None)
    formatted_pickup_datetime = utc_pickup_datetime.strftime("%Y-%m-%d %H:%M:%S UTC")
    dict_data={"key":["2013-07-06 17:18:00.000000119"],
        "pickup_datetime": [formatted_pickup_datetime],
  "pickup_longitude": [float(pickup_longitude)],
  "pickup_latitude": [float(pickup_latitude)],
  "dropoff_longitude":[float(dropoff_longitude)],
  "dropoff_latitude": [float(dropoff_latitude)],
  "passenger_count": [int(passenger_count)]
    }
    X_pred=pd.DataFrame(dict_data)
    model=joblib.load("model.joblib")
    prediction=model.predict(X_pred)
    return {'fare':prediction[0]}