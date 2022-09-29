from unittest.mock import MagicMock, patch
import pytest

pytestmark = pytest.mark.django_db


def get_dummy_api_response(lat, lon):
    return {
        "coord": {"lon": lon, "lat": lat},
        "weather": [
            {"id": 803, "main": "Clouds", "description": "broken clouds", "icon": "04d"}
        ],
        "base": "stations",
        "main": {
            "temp": 123123298.2,
            "feels_like": 298.88,
            "temp_min": 298.2,
            "temp_max": 298.2,
            "pressure": 1011,
            "humidity": 81,
            "sea_level": 1011,
            "grnd_level": 1011,
        },
        "visibility": 10000,
        "wind": {"speed": 7.15, "deg": 224, "gust": 7.31},
        "clouds": {"all": 55},
        "dt": 567456,
        "sys": {"sunrise": 123234, "sunset": 345456567},
        "timezone": 0,
        "id": 0,
        "name": "",
        "cod": 200,
    }


def test_getting_todays_weather(api_client):
    lat = 44
    lon = 55

    api_mock = MagicMock(return_value=get_dummy_api_response(lat, lon))
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
