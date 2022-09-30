"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_simplejwt import views as jwt_views
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class HealthCheck(APIView):
    permission_classes = [AllowAny]

    def get(self, _):
        return HttpResponse("OK\n", status=200)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("backend.apps.account.urls")),
    path("weather/", include("backend.apps.weather.urls")),
    path("api/token/", jwt_views.TokenObtainPairView.as_view(), name="token-get"),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token-refresh"
    ),
    path("health", HealthCheck.as_view(), name="health"),
]
