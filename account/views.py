from django.contrib.auth import authenticate

# from django.shortcuts import render
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import LoginUserSerializer, RegisterUserSerializer


class RegisterUserView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()


class LoginUserView(CreateAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        email = request.data["email"]
        password = request.data["password"]
        user = authenticate(email=email, password=password)

        if user is None:
            raise AuthenticationFailed(
                "Пользователь с такими учетными данными не найден!"
            )

        if not user.check_password(password):
            raise AuthenticationFailed("Неверный пароль!")

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "status": "Вы, успешно авторизовались!",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )
