# from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""

    # referral_code = serializers.CharField(
    # max_length=255,
    # write_only=True,
    # required=False,
    # allow_blank=True
    # )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "number",
            "first_name",
            "last_name",
            "password",
            "referral_code",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        """
        Creates new user with/without referral code.
        """
        """
        referred_by = ''
        referral_code = validated_data.pop('referral_code')
        try:
            referred_by = User.objects.get(referral_token=referral_code)
        except ObjectDoesNotExist:
            pass
        """
        password = validated_data["email"]
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        """
        if referred_by:
            referral = Referral.objects.create(
                referred_by=referred_by,
                referred_to=user
                )
            referral.save()
        """
        return user


class ChangePassword(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','password']

class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]


class MailReferralSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "referral_code"]
