import random
import string

from django.conf import settings
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser

from .models import User
from .serializers import (
    LoginUserSerializer,
    RegisterUserSerializer,
    ChangePasswordSerializer,
    MailChangePasswordSerializer
)

import django_filters
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from account.models import User
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated


class RegisterUserView(generics.ListCreateAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()
    search_fields = ["phone_number", "email"]
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        subject = "Referral code for Mega_calendar"
        message = "По умолчанию ваш пароль, это ваш email. Для логина перейдите по ссылке http://localhost:8000/login/"
        recipient = email
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [recipient],
            fail_silently=False,
        )
        return self.create(request, *args, **kwargs)

class LoginUserView(CreateAPIView):
    serializer_class = LoginUserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, username=email, password=password)

        if user is None:
            raise AuthenticationFailed(
                "Пользователь с такими учетными данными не найден!"
            )

        refresh = RefreshToken.for_user(user)
        
        return Response(
            {
                "status": "Вы, успешно авторизовались!",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )


class MailPasswordChangeView(APIView):
    serializer_class = MailChangePasswordSerializer
    queryset = User.objects.all()
    # permission_classes = (IsSuperuser, )

    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        letters = string.ascii_letters
        new_password = "".join(random.choice(letters) for i in range(10))
        user = User.objects.filter(email=email).first()
        user.set_password(new_password)
        user.save()
        subject = "New password for Mega_calendar"
        message = new_password
        recipient = email
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [recipient],
            fail_silently=False,
        )
        return Response(
            {"статус": ("Пароль успешно изменён, проверьте свою почту")}
        )


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)