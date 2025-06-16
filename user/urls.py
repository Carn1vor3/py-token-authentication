from django.urls import include, path
from rest_framework.authtoken import views

from user.views import CreateUserView, LoginUserView, ManageUserView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="user_register"),
    path("login/", LoginUserView.as_view(), name="user_login"),
    path("me/", ManageUserView.as_view(), name="user_me"),
]

app_name = "user"
