from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response

from .api import WeatherAPI


class WeatherToday(APIView):
    def get(self, request):
        user = request.user
        query_params = request.query_params

        if "lat" in query_params and "lon" in query_params:
            latitude = query_params["lat"]
            longitude = query_params["lon"]
        else:
            if not user:
                return Response({"error": "lat and lon are required"}, 400)
            if not user.favourite_coords:
                return Response(
                    {
                        "error": "lat and lon are required ; consider adding your favourite coords "
                    },
                    400,
                )
            coords = user.favourite_coords.first()
            latitude = coords.lat
            longitude = coords.lon

        def get_data(lat, lon):
            key = f"{lat}-{lon}"
            if key in cache:
                return cache.get(key)
            data = WeatherAPI().get_current_weather(lat, lon)
            cache.set(key, data, timeout=60 * 60 * 3)  # 3h
            return data

        return Response({"data": get_data(float(latitude), float(longitude))})
