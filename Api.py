import requests
from dotenv import load_dotenv
import os 
import json
from requests.exceptions import HTTPError

load_dotenv()

def request(city) :
    if city == None :
        return None
    payload = {
            "q" : city,
            "APPID" : os.getenv("API_KEY")
            }
    url = "https://api.openweathermap.org/data/2.5/weather"
    try:
        response = requests.get(url, params=payload)
        response.raise_for_status()
    except HTTPError as err :
        print(err)
        return None
    else :
        return response.json()
        
def validate_city(city) :
    headers = {
            "User-agent" : "weather-app/1.0"
            }
    payload = {
        
            "q" : city ,
            "format" : "json",
            "limit" : 5,

            }
    url = "https://nominatim.openstreetmap.org/search"
    response = requests.get(url, params=payload, headers=headers)
    data = response.json()
    for place in data :
        if place.get("type") in ["city", "administrative"] and place.get("addresstype") == "city":
            return city
    return None
