from django.urls import path
from . import views

urlpatterns = [path("today/", views.WeatherToday.as_view(), name="weather-today")]
