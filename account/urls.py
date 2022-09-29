from django.urls import path

from account.views import (
    ChangePasswordView,
    LoginUserView,
    MailPasswordChangeView,
    RegisterUserView,
    UpdateDestroyUser,
    UpdateUserAPIDetail,
    FirstLoginView
)

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="createuser"),
    path("login/", LoginUserView.as_view(), name="authuser"),
    path(
        "change_user/<int:pk>", UpdateDestroyUser.as_view(), name="update_user"
    ),
    path(
        "update_user/<int:pk>", UpdateUserAPIDetail.as_view(), name="update_for_users"
    ),
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
    path("first_login/",FirstLoginView.as_view(),name="first_login")
]
