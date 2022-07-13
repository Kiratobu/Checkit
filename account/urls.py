from django.urls import path
from account.views import LoginUserView, RegisterUserView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="createuser"),
    path("login/", LoginUserView.as_view(), name="authuser"),
]