from django.urls import path

from account.views import LoginUserView, RegisterUserView,MailPasswordChangeView, ChangePasswordView

urlpatterns = [
    path("register/", RegisterUserView.as_view(), name="createuser"),
    path("login/", LoginUserView.as_view(), name="authuser"),
    path("mail_change_password/", MailPasswordChangeView.as_view(), name="mail_password_change"),
    path('change-password/', ChangePasswordView.as_view(), name='change-password')
]