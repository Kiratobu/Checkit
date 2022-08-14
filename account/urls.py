from django.urls import path

from account.views import (
    ChangePasswordView,
    LoginUserView,
    MailPasswordChangeView,
    RegisterUserView,
    UpdateDestroyUser
)

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="createuser"),
    path("login/", LoginUserView.as_view(), name="authuser"),
    path("change_user/<int:pk>", UpdateDestroyUser.as_view(), name="update_user"),
    path(
        "mail_change_password/",
        MailPasswordChangeView.as_view(),
        name="mail_password_change",
    ),
    path(
        "change_password/",
        ChangePasswordView.as_view(),
        name="change-password",
    ),
]
