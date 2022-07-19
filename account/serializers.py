from rest_framework import serializers

from .models import User


class RegisterUserSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "number",
            "first_name",
            "last_name",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def create(self, validated_data):
        """
        Creates new user with/without referral code.
        """
    
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        
        return user


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]
        
class ChangePassword(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email']

