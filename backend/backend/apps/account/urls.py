from django.urls import path

from .views import RegisterApiView

urlpatterns = [
    path("register/", RegisterApiView.as_view()),
]
