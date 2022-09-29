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

        return Response({"data": WeatherAPI().get_current_weather(latitude, longitude)})
