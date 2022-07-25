from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from .managers import UserManager
from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractBaseUser, PermissionsMixin, TimeStampModel):
    """User model"""

    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    phone_number = models.CharField(max_length=20, unique=True, null=False)
    email = models.CharField(
        max_length=30, blank=False, unique=True, null=False
    )
    is_staff = models.BooleanField(default=False)
    image = models.ImageField(default=None, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list = []

    objects = UserManager()

    def __str__(self):
        return self.email

    """
    def save(self, *args, **kwargs):
        self.referral_token = f'{self.email}&{get_random_string(length=30)}'
        super().save(*args, **kwargs)
    """
