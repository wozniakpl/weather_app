import pytest

from django.contrib.auth import get_user_model


User = get_user_model()

pytestmark = pytest.mark.django_db


def test_registering(api_client):
    assert User.objects.count() == 0
    response = api_client.post(
        "/account/register/",
        {
            "username": f"test",
            "password": "AVerySafeAngLong!P4$$word",
            "first_name": "Test",
            "last_name": "User",
        },
    )
    assert response.status_code == 201, response.json()
    data = response.json()

    assert User.objects.count() == 1
    user = User.objects.first()

    assert user.username == "test" == data["username"]
    assert user.first_name == "Test" == data["first_name"]
    assert user.last_name == "User" == data["last_name"]
    assert user.check_password("AVerySafeAngLong!P4$$word")
