from django.urls import path
from account.views import LoginUserView, RegisterUserView, PasswordChangeView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="createuser"),
    path("login/", LoginUserView.as_view(), name="authuser"),
    path("change_password", PasswordChangeView.as_view(), name="password_change")
]