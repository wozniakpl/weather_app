from django.urls import path

from .views import RegisterApiView, UserApiView, FavouriteCoordsView

urlpatterns = [
    path("register/", RegisterApiView.as_view()),
    path("user/", UserApiView.as_view()),
    path("favourite-coords/", FavouriteCoordsView.as_view()),
]
