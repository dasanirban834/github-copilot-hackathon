############## Import modules ##############
import requests
import json
from tabulate import tabulate
import os

############## Call System Variable 'Color' ##############
os.system('color')
############# Define the user inputs ###############
city = input("Please enter the city name: ")
print('\n')
api_key = ''
with open('credentials.json', 'r') as r:
    read_text = r.read()
    credentials = json.loads(read_text)
    api_key = credentials['api_key']

############## Get the latitude and longitude of the city ##############
url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}"
resp = requests.get(url)
data = json.loads(resp.text)
Latitude = data[0]['lat']
Longitude = data[0]['lon']

############## Define the class ##############
class Weather():
    ############# Initializing variables ###############
    def __init__(self, api_key, city, Latitude, Longitude):
        self.api_key = api_key
        self.city = city
        self.Latitude = Latitude
        self.Longitude = Longitude
    ############# Current weather updates function ###############
    def get_weather(self):
        base_url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": self.city,
            "appid": self.api_key,
            "units": "Metric"  # You can change the unit to "imperial" for Fahrenheit
        }
        response = requests.get(base_url, params=params)
        weather_data = json.loads(response.text)
        CurrentTemperature =  weather_data['main']['temp']
        FeelsLike =  weather_data['main']['feels_like']
        MinimumTemperature =  weather_data['main']['temp_min']
        MaximumTemperature =  weather_data['main']['temp_max']
        Humidity =  weather_data['main']['humidity']
        Pressure = weather_data['main']['pressure']
        WindSpeed =  weather_data['wind']['speed']
        WindDirection =  weather_data['wind']['deg']
        WeatherCondition =  weather_data['weather'][0]['main']
        WeatherCode = str(weather_data['weather'][0]['id'])
        s1 = '\x1B[1m' + 'Todays Weather Updates:' + '\x1B[0m'
        print(f"\n{s1}\n\nCity Name --> {city} \t\tCurrent Temperature --> {CurrentTemperature}°C \nFeels Like --> {FeelsLike}°C \t\tMinimum/Maximum --> {MinimumTemperature}°C/{MaximumTemperature}°C \nHumidity --> {Humidity}% \t\tPressure --> {Pressure} \nWind Speed --> {WindSpeed}m/s \t\tWeather Code --> {WeatherCode}")
        ############# Calling description function ###############
        from weathercode import description
        description(WeatherCode)
        s2 = '\x1B[1m' + 'Air Quality Index Table:' + '\x1B[0m'
        print(f'\n{s2}\n')
        ############# Calling AQI function ###############
        from aqi import currentAQI
        currentAQI(Latitude, Longitude, city)
        ############ Calling Forecasting function ############
        from forecasting import forecasting
        forecasting(city, api_key, Latitude, Longitude)
    

############## Calling the class ##############
obj = Weather(api_key, city, Latitude, Longitude)
obj1 = obj.get_weather()
print(obj1)