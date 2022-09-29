# from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "phone_number",
            "first_name",
            "last_name",
        ]

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

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "image",
            "first_name",
            "last_name",
        ]


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]


class MailChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email"]


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    
class FirstLoginSerializer(serializers.ModelSerializer):
    new_password = serializers.CharField(required=True)
    check_password = serializers.CharField(required=True)
    
    class Meta:
        model = User
        """
        Serializer for first login endpoint.
        """
        fields = ["image","new_password","check_password"]
    