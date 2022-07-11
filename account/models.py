# from email.policy import default

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models

# from django.utils.crypto import get_random_string


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, **extra_fields):
        """
        Methode creates user
        :param email: str
        :param name: str
        :param surname: str
        :param extra_fields: dict
        :return: user
        """
        if not email:
            raise ValueError("Вы должны ввести свою электронную почту")
        if not first_name or not last_name:
            raise ValueError("Вы должны ввести свое Имя/Фамилию")

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            **extra_fields,
        )
        user.set_password()
        user.save()
        return user

    def create_superuser(self, email, password):
        """
        Methode creates superuser
        :param email: str
        :param password: str
        :return: superuser
        """
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin, TimeStamp):
    """User model"""

    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    number = models.CharField(max_length=20, unique=True, null=False)
    email = models.CharField(
        max_length=30, blank=False, unique=True, null=False
    )
    # referral_token = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    img = models.ImageField(default=None, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list = []

    objects = UserManager()

    def __str__(self):
        return f"{self.email}"

    """
    def save(self, *args, **kwargs):
        self.referral_token = f'{self.email}&{get_random_string(length=30)}'
        super().save(*args, **kwargs)
    """
