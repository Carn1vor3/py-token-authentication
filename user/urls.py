from django.urls import include, path
from rest_framework.authtoken import views

from user.views import CreateUserView, LoginUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="user_register"),
    path("login/", LoginUserView.as_view(), name="user_login"),
]

app_name = "user"
