from unittest.mock import MagicMock, patch
import pytest

from .fixtures import (
    get_dummy_api_response_for_next_days,
    get_dummy_api_response_for_today,
)

pytestmark = pytest.mark.django_db


def test_getting_todays_weather(api_client):
    lat = 44
    lon = 55

    api_mock = MagicMock(return_value=get_dummy_api_response_for_today(lat, lon))
    with patch("backend.apps.weather.api.WeatherAPI.get_current_weather", api_mock):
        response = api_client.get(f"/weather/today/?lat={lat}&lon={lon}")
        assert api_mock.called
        assert response.status_code == 200
        data = response.json()["data"]
        assert data["main"]["temp"] == 123123298.2  # so I know it used the mock
        assert data["coord"]["lat"] == lat
        assert data["coord"]["lon"] == lon
        assert data["weather"][0]["main"] == "Clouds"
        assert data["weather"][0]["description"] == "broken clouds"


def test_caching_data(api_client):
    lat = 22
    lon = 33
    url = f"/weather/today/?lat={lat}&lon={lon}"
    api_mock = MagicMock(return_value=get_dummy_api_response_for_today(lat, lon))
    with patch("backend.apps.weather.api.WeatherAPI.get_current_weather", api_mock):
        first_response = api_client.get(url)
        assert api_mock.called

    api_mock = MagicMock()
    with patch("backend.apps.weather.api.WeatherAPI.get_current_weather", api_mock):
        second_response = api_client.get(url)
        assert not api_mock.called

    assert first_response.json() == second_response.json()


def test_getting_weather_for_next_days(api_client):
    lat = 44
    lon = 55
    url = f"/weather/next-days/?lat={lat}&lon={lon}"
    api_mock = MagicMock(return_value=get_dummy_api_response_for_next_days(lat, lon))
    with patch(
        "backend.apps.weather.api.WeatherAPI.get_weather_for_next_days", api_mock
    ):
        response = api_client.get(url)
        assert api_mock.called
        assert response.status_code == 200
        data = response.json()["data"]
        assert data["city"]["coord"]["lat"] == lat
        assert data["city"]["coord"]["lon"] == lon
        assert data["list"][0]["main"]["temp"] == 295.03
