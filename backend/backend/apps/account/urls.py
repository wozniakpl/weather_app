from django.urls import path

from .views import RegisterApiView, UserApiView

urlpatterns = [
    path("register/", RegisterApiView.as_view()),
    path("user/", UserApiView.as_view()),
]
