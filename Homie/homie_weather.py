import os

import requests
from geopy.geocoders import Nominatim


def is_gonna_rain(city):
    geolocator = Nominatim(user_agent="homie")
    location = geolocator.geocode(city)
    if location is not None:
        params = {
            'lat': location.latitude,
            'lon': location.longitude,
            'appid': os.environ['open_weather_map_key'],
        }

        data = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=params)
        data.raise_for_status()
        weather_data = data.json()['list'][:4]
        for i in weather_data:
            if i['weather'][0]['id'] < 700:
                return f'al parecer en {location.address}, es probable que llueva en las próximas 12 horas'
        return f'al parecer en {location.address}, no es muy probable que llueva en las próximas 12 horas'
    else:
        return f'lo siento, no pude encontrar el sitio'


def get_temp(city):
    geolocator = Nominatim(user_agent="homie")
    location = geolocator.geocode(city)
    if location is not None:
        params = {
            'lat': location.latitude,
            'lon': location.longitude,
            'appid': os.environ['open_weather_map_key'],
        }

        data = requests.get('http://api.openweathermap.org/data/2.5/forecast', params=params)
        data.raise_for_status()
        temp_data = data.json()['list'][0]['main']['temp']
        temp_data -= 273.15
        return f'al parecer en {location.address}, el promedio de temperatura en las próximas 3 ' \
               f'horas sera de {"%.2f" % temp_data} grados'
    else:
        return f'lo siento, no pude encontrar el sitio'
