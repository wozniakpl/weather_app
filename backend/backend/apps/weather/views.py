from this import d
from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import AnonymousUser

from .api import WeatherAPI


def get_coords(query_params, user):
    if "lat" in query_params and "lon" in query_params:
        latitude = query_params["lat"]
        longitude = query_params["lon"]
    else:
        if not user or isinstance(user, AnonymousUser):
            return Response({"error": "lat and lon are required"}, 400)
        if not hasattr(user, "favourite_coords"):
            return Response(
                {
                    "error": "lat and lon are required ; consider adding your favourite coords "
                },
                400,
            )
        coords = user.favourite_coords.first()
        latitude = coords.lat
        longitude = coords.lon
    return latitude, longitude


def cached(key, getter):
    if key in cache:
        return cache.get(key)
    data = getter()
    cache.set(key, data, timeout=60 * 60 * 3)  # 3h
    return data


class WeatherToday(APIView):
    def get(self, request):
        latitude, longitude = get_coords(request.query_params, request.user)

        def get_data(lat, lon):  # TODO: typing
            return cached(
                f"{lat}-{lon}-today", lambda: WeatherAPI().get_current_weather(lat, lon)
            )

        return Response({"data": get_data(float(latitude), float(longitude))})


class WeatherNextDays(APIView):
    def get(self, request):
        latitude, longitude = get_coords(request.query_params, request.user)

        def get_data(lat, lon):  # TODO: typing
            return cached(
                f"{lat}-{lon}-next-days",
                lambda: WeatherAPI().get_weather_for_next_days(lat, lon),
            )

        return Response({"data": get_data(float(latitude), float(longitude))})


# TODO; error handling
