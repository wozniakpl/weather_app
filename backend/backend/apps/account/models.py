from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class FavouriteCoords(models.Model):
    # TODO; one to one
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favourite_coords"
    )
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.lat}, {self.lon})"
