from unittest.mock import MagicMock, patch
import pytest
from django.core.cache import cache


def register_and_login(api_client):
    register_response = api_client.post(
        "/account/register/",
        {
            "username": "test",
            "password": "AVerySafeAngLong!P4$$word",
            "first_name": "Test",
            "last_name": "User",
        },
    )
    assert register_response.status_code == 201, register_response.json()
    login_response = api_client.post(
        "/api/token/",
        {
            "username": "test",
            "password": "AVerySafeAngLong!P4$$word",
        },
    )
    assert login_response.status_code == 200, login_response.json()
    assert "access" in login_response.json()
    assert "refresh" in login_response.json()

    access_token = login_response.json()["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    user_response = api_client.get("/account/user/")
    assert user_response.status_code == 200
    assert user_response.json()["username"] == "test"


@pytest.mark.django_db
def test_setting_favourite_coords(api_client):
    register_and_login(api_client)

    user_response = api_client.get("/account/user/")
    assert user_response.status_code == 200
    assert user_response.json()["username"] == "test"
    assert user_response.json()["favourite_coords"] is None

    lat = 23
    lon = 34

    response = api_client.post(
        "/account/favourite-coords/",
        {
            "lat": lat,
            "lon": lon,
        },
    )
    assert response.status_code == 200, response.json()

    user_response = api_client.get("/account/user/")
    assert user_response.status_code == 200
    assert user_response.json()["username"] == "test"
    assert user_response.json()["favourite_coords"] == {
        "lat": lat,
        "lon": lon,
    }

    mock_1 = MagicMock(return_value={"data": "mocked-1"})
    with patch(
        "backend.apps.weather.api.WeatherAPI.get_current_weather",
        mock_1,
    ):
        default_weather_response = api_client.get("/weather/today/")
        assert (
            default_weather_response.status_code == 200
        ), default_weather_response.json()

    # when called, cache will be used
    # and `call_args` won't be available
    # that's why there's a cache clear here
    # simulatiing the time passing between calls
    cache.clear()
    mock_2 = MagicMock(return_value={"data": "mocked-2"})
    with patch(
        "backend.apps.weather.api.WeatherAPI.get_current_weather",
        mock_2,
    ):
        explicit_weather_response = api_client.get(
            f"/weather/today/?lat={lat}&lon={lon}"
        )
        assert (
            explicit_weather_response.status_code == 200
        ), explicit_weather_response.json()

    assert mock_1.call_args == mock_2.call_args

    response = api_client.post(
        "/account/favourite-coords/",
        {
            "lat": lat + 1,
            "lon": lon + 1,
        },
    )
    assert response.status_code == 200, response.json()

    user_response = api_client.get("/account/user/")
    assert user_response.status_code == 200
    assert user_response.json()["username"] == "test"
    assert user_response.json()["favourite_coords"] == {
        "lat": lat + 1,
        "lon": lon + 1,
    }
