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

from .models import User
from .serializers import (
    ChangePassword,
    LoginUserSerializer,
    RegisterUserSerializer,
    ChangePassword,
)

from rest_framework.views import APIView
import django_filters
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics

class RegisterUserView(generics.ListCreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()
    search_fields = ["number", "email"]
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        subject = "Referral code for Mega_calendar"
        message = "http://localhost:8000/login/"
        recipient = email
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [recipient],
            fail_silently=False,
        )
        return self.create(request, *args, **kwargs)

class PasswordChangeView(APIView):
    serializer_class = ChangePassword
    queryset = User.objects.all()
    # permission_classes = (IsSuperuser, )

    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]

        user = User.objects.filter(email=email).first()
        user.set_password(password)
        user.save()
        return Response({"статус": ("Пароль успешно изменён")})

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
                "first_name": user.first_name,
                "last_name" : user.last_name,
                "number": user.number,
                "email" :user.email,
                "is_staff" : user.is_staff,
                #"img" : user.img,
                "date_of_birth" : user.date_of_birth,
                "is_active" : user.is_active
            }
        )


class PasswordChangeView(APIView):
    serializer_class = ChangePassword
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
