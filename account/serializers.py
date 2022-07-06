# from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers

from .models import Event, EventType, User, UserParticipant


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
            # "referral_code",
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
        password = validated_data.pop("password")
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


class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password"]


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "number",
            "first_name",
            "last_name",
        ]


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class UserParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserParticipant
        fields = "__all__"


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        models = EventType
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
