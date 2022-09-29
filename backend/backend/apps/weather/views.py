from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response

from .api import WeatherAPI


class WeatherToday(APIView):
    def get(self, request):
        query_params = request.query_params

        if not ("lat" in query_params and "lon" in query_params):
            return Response({"error": "lat and lon are required"}, 400)

        latitude = query_params["lat"]
        longitude = query_params["lon"]

        def get_data(lat, lon):
            key = f"{lat}-{lon}"
            if key in cache:
                return cache.get(key)
            data = WeatherAPI().get_current_weather(lat, lon)
            cache.set(key, data, timeout=60 * 60 * 3)  # 3h
            return data

        return Response({"data": get_data(latitude, longitude)})
