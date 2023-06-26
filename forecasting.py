import json
import requests
from tabulate import tabulate
import datetime

def forecasting(city, api_key, Latitude, Longitude):
        ## weather upcoming days
        base_url = "https://api.openweathermap.org/data/2.5/forecast/"
        params = {
            "q": city,
            "appid": api_key,
            "units": "Metric",  # You can change the unit to "imperial" for Fahrenheit
            "mode": "json"
        }
        response = requests.get(base_url, params=params)
        weather_data = json.loads(response.text)
        timestamp = []
        avgTemperature = []
        humidity = []
        precipitation = []
        s1 = '\x1B[1m' + 'Forecasted Weather Report:' + '\x1B[0m'
        print(f"\n{s1}", '\n')
        for i in range(1, len(weather_data['list'])):
            SRNo = i
            Timestamp = weather_data['list'][i]['dt_txt']
            Timestamp_datetime = datetime.datetime.strptime(Timestamp, '%Y-%m-%d %H:%M:%S')
            Timestamp = Timestamp_datetime.strftime("%d") + ' ' + Timestamp_datetime.strftime("%b") + '\'' + Timestamp_datetime.strftime("%Y").split("20")[1] + ' ' + Timestamp_datetime.strftime("%H") + ':' + Timestamp_datetime.strftime("%M")
            timestamp.append(Timestamp)
            FeelsLike = weather_data['list'][i]['main']['feels_like']
            AvgTemperature = weather_data['list'][i]['main']['temp']
            avgTemperature.append(AvgTemperature)
            MaximumTemperature = weather_data['list'][i]['main']['temp_max']
            MinimumTemperature = weather_data['list'][i]['main']['temp_min']
            Humidity = weather_data['list'][i]['main']['humidity']
            humidity.append(Humidity)
            WeatherCondition = weather_data['list'][i]['weather'][0]['main']
            WeatherCode = weather_data['list'][i]['weather'][0]['id']
            WindSpeed = weather_data['list'][i]['wind']['speed']
            Precipitation = weather_data['list'][i]['pop'] * 100
            precipitation.append(Precipitation)
            visibility = weather_data['list'][i]['visibility']
            table = [
                ["Interation", "Timestamp", "Feels Like(°C)", "Average Temperature", "Maximum Temperature(°C)", "Minimum Temperature(°C)", "Humidity(%)", "Weather Condition", "Weather Code", "Wind Speed(m/s)", "Precipitation", "Visibility(m)"],
                [SRNo, Timestamp, FeelsLike, AvgTemperature, MaximumTemperature, MinimumTemperature, Humidity, WeatherCondition, WeatherCode, WindSpeed, Precipitation, visibility]
            ]
            table = tabulate(table, tablefmt="grid", colalign=("center" for i in range(11)))
            print(table)

        s2 = '\x1B[1m' + 'Forecasted AQI Report:' + '\x1B[0m'
        print(f"\n{s2}", '\n')

        from aqi import forecastedAQI
        x_aqi = forecastedAQI(Latitude, Longitude, city, api_key)
        y_gas = x_aqi[0]
        z_time = x_aqi[1]
        from graph import graph
        graph(avgTemperature, humidity, precipitation, timestamp, y_gas, z_time)