from django.conf import settings
from django.contrib.auth import authenticate
from django.core.mail import send_mail
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


from .models import User
from .serializers import (
    LoginUserSerializer,
    RegisterUserSerializer,
    ChangePassword
)


class RegisterUserView(CreateAPIView):
    serializer_class = RegisterUserSerializer
    queryset = User.objects.all()
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


class LoginUserView(CreateAPIView):
    serializer_class = LoginUserSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, username=email, password=password)

        if user is None:
            raise AuthenticationFailed(
                f"{user} Пользователь с такими учетными данными не найден!"
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "status": "Вы, успешно авторизовались!",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )
        
        
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
