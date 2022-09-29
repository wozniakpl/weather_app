import json
import requests

from django.conf import settings


class WeatherAPI:
    def __init__(self, api_key=None):
        self.api_key = api_key or settings.OPENWEATHERMAP_API_KEY

    def get_current_weather(self, lat, lon):
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.api_key}"
        return json.loads(requests.get(url).text)
