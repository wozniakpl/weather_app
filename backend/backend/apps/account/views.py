from rest_framework import generics, permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer


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
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response(
            UserSerializer(request.user, context=self.get_serializer_context()).data,
            200,
        )
