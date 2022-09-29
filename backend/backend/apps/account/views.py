from django.db import transaction

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RegisterSerializer, UserSerializer, CoordsSerializer
from .models import FavouriteCoords


class RegisterApiView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            UserSerializer(user, context=self.get_serializer_context()).data,
            201,
        )


class UserApiView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(
            UserSerializer(request.user, context=self.get_serializer_context()).data,
            200,
        )


class FavouriteCoordsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        body = request.data
        if "lat" not in body or "lon" not in body:
            return Response(
                {
                    "status": "ERROR",
                    "message": "lat and lon must be provided",
                },
                400,
            )

        request.user.favourite_coords.all().delete()
        FavouriteCoords.objects.create(
            user=request.user,
            lat=body["lat"],
            lon=body["lon"],
        )
        return Response({"status": "OK"}, 200)

    def get(self, request, *args, **kwargs):
        return Response(
            CoordsSerializer(request.user.favourite_coords).data,
            200,
        )
