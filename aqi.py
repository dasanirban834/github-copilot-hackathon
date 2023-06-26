import requests
import json
from tabulate import tabulate
import datetime

api_key = ''
with open('credentials.json', 'r') as r:
    read_text = r.read()
    credentials = json.loads(read_text)
    api_key = credentials['api_key']

def currentAQI(Latitude, Longitude, city):
    base_url = "http://api.openweathermap.org/data/2.5/air_pollution"
    params = {
        "lat": Latitude,
        "lon": Longitude,
        "appid": api_key
    }
    response = requests.get(base_url, params=params)
    aqi_data = json.loads(response.text)
    aqi = aqi_data['list'][0]['main']['aqi']
    co = int(aqi_data['list'][0]['components']['co'])
    no = int(aqi_data['list'][0]['components']['no'])
    no2 = int(aqi_data['list'][0]['components']['no2'])
    o3 = int(aqi_data['list'][0]['components']['o3'])
    so2 = int(aqi_data['list'][0]['components']['so2'])
    pm_25 = int(aqi_data['list'][0]['components']['pm2_5'])
    pm10 = int(aqi_data['list'][0]['components']['pm10'])
    nh3 = int(aqi_data['list'][0]['components']['nh3'])
    gas = [co, no, no2, o3, so2, pm_25, pm10, nh3]

    if aqi == 1:
        category = "Good"
        table = [
                ["City", "AQI", "Category", "CO", "NO2", "O3", "SO2", "PM2.5", "PM10"],
                [city, aqi, category, co, no2, o3, so2, pm_25, pm10]
            ]
        table = tabulate(table, tablefmt="grid", colalign=("center" for i in range(9)))
        print(table)
    
    if aqi == 2:
        category = "Fair"
        table = [
                ["City", "AQI", "Category", "CO", "NO2", "O3", "SO2", "PM2.5", "PM10"],
                [city, aqi, category, co, no2, o3, so2, pm_25, pm10]
            ]
        table = tabulate(table, tablefmt="grid", colalign=("center" for i in range(9)))
        print(table)
    
    if aqi == 3:
        category = "Moderate"
        table = [
                ["City", "AQI", "Category", "CO", "NO2", "O3", "SO2", "PM2.5", "PM10"],
                [city, aqi, category, co, no2, o3, so2, pm_25, pm10]
            ]
        table = tabulate(table, tablefmt="grid", colalign=("center" for i in range(9)))
        print(table)

    if aqi == 4:
        category = "Poor"
        table = [
                ["City", "AQI", "Category", "CO", "NO2", "O3", "SO2", "PM2.5", "PM10"],
                [city, aqi, category, co, no2, o3, so2, pm_25, pm10]
            ]
        table = tabulate(table, tablefmt="grid", colalign=("center" for i in range(9)))
        print(table)

    if aqi == 5:
        category = "Very Poor"
        table = [
                ["City", "AQI", "Category", "CO", "NO2", "O3", "SO2", "PM2.5", "PM10"],
                [city, aqi, category, co, no2, o3, so2, pm_25, pm10]
            ]
        table = tabulate(table, tablefmt="grid", colalign=("center" for i in range(9)))
        print(table)
