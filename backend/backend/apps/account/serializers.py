from rest_framework import serializers
from django.contrib.auth.models import User
from backend.apps.account.models import FavouriteCoords


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "first_name", "last_name")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        return User.objects.create_user(
            validated_data["username"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteCoords
        exclude = ("user", "id")


class UserSerializer(serializers.ModelSerializer):
    # favourite_coords = CoordsSerializer(read_only=True)

    favourite_coords = serializers.SerializerMethodField()

    def get_favourite_coords(self, obj):
        if not obj.favourite_coords.exists():
            return None
        return CoordsSerializer(obj.favourite_coords.first()).data

    class Meta:
        model = User
        fields = "__all__"
