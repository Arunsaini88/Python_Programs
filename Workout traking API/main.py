import requests
import os
from datetime import datetime
SHEET_PUT_API = "https://api.sheety.co/fa12d6a2184ca52313e16eea71b5c6ca/workoutsTracking/workouts"

GENDER = "MALE"
WEIGHT_KG = "60"
HEIGHT = "160.5"  # entered random height in cm
AGE = "50"

APP_ID = "Add your workout API ID"
API_KEY = "Add your workout API Key"

exercise_endpoint = "put the exercise end point"

exercise_input = input("Tell which exercise you did today?: ")

header = {
    "x-app-id": APP_ID,
    'x-app-key': API_KEY
}

parameters = {
    'query': exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
response.raise_for_status()
bearer_header = {
    "Authorization": "Bearer @dsjfwqeu7sa\f7dfhfjjfgf4hg5sa8sg",
}
today_date = datetime.now().strftime("%d/%m/%Y")
today_time = datetime.now().strftime("%X")
result = response.json()
exercises = result['exercises']
for exercise_ in exercises:
    sheet_dict = {
        "workout":{
            "time":today_time,
            "date":today_date,
            "exercise":exercise_["name"].title(),
            "duration":exercise_["duration_min"],
            "calories":exercise_["nf_calories"]
        }
    }
    sheet_response = requests.post(SHEET_PUT_API, json=sheet_dict, auth=("arun1saini", "Arun@123"))

    print(sheet_response.text)
