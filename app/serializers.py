from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from rest_framework import serializers

from account.models import User
from account.serializers import RegisterUserSerializer
from app.models import (
    Branch,
    BranchPost,
    Event,
    EventType,
    Notification,
    Organisation,
    Post,
    Room,
    UserParticipant,
    UserPost,
)


# mypy: ignore-errors
class OrganisationSerializer(serializers.ModelSerializer):
    branches = serializers.StringRelatedField(many=True)
    organisation_admin = PresentablePrimaryKeyRelatedField(
        queryset=User.objects.all(),
        presentation_serializer=RegisterUserSerializer,
    )

    class Meta:
        model = Organisation
        fields = ["title", "organisation_admin", "branches"]

    def create(self, validated_data):
        branches_data = validated_data.pop("branches")
        organisation = Organisation.objects.create(**validated_data)
        for branch_data in branches_data:
            Organisation.objects.create(
                organisation=organisation, **branch_data
            )
        return organisation


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class BranchSerializer(serializers.ModelSerializer):
    head_branch = PresentablePrimaryKeyRelatedField(
        queryset=User.objects.all(),
        presentation_serializer=RegisterUserSerializer,
    )
    organisation = PresentablePrimaryKeyRelatedField(
        queryset=Organisation.objects.all(),
        presentation_serializer=OrganisationSerializer,
    )

    class Meta:
        model = Branch
        fields = "__all__"

    def create(self, validated_data):
        return Branch.objects.create(**validated_data)


class UserPostSerializer(serializers.ModelSerializer):
    user = PresentablePrimaryKeyRelatedField(
        queryset=User.objects.all(),
        presentation_serializer=RegisterUserSerializer,
    )
    post = PresentablePrimaryKeyRelatedField(
        queryset=Post.objects.all(), presentation_serializer=PostSerializer
    )

    class Meta:
        model = UserPost
        fields = "__all__"

    def create(self, validated_data):
        return UserPost.objects.create(**validated_data)


class BranchPostSerializer(serializers.ModelSerializer):
    post = PresentablePrimaryKeyRelatedField(
        queryset=Post.objects.all(), presentation_serializer=PostSerializer
    )
    branch = PresentablePrimaryKeyRelatedField(
        queryset=Branch.objects.all(), presentation_serializer=BranchSerializer
    )

    class Meta:
        model = BranchPost
        fields = "__all__"

    def create(self, validated_data):
        return BranchPost.objects.create(**validated_data)


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

    def create(self, validated_data):
        return Room.objects.create(**validated_data)


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"

    def create(self, validated_data):
        return Notification.objects.create(**validated_data)


class EventSerializer(serializers.ModelSerializer):
    notifications = serializers.StringRelatedField(many=True)
    room = PresentablePrimaryKeyRelatedField(
        queryset=Room.objects.all(),
        presentation_serializer=RoomSerializer,
    )

    class Meta:
        model = Event
        fields = [
            "title",
            "date",
            "description",
            "created_at",
            "updated_at",
            "time_from",
            "time_to",
            "repeat",
            "is_private",
            "event_type",
            "notifications",
            "room",
        ]

    def create(self, validated_data):
        notifications_data = validated_data.pop("notifications")
        event = Event.objects.create(**validated_data)
        for notification_data in notifications_data:
            Event.objects.create(event=event, **notification_data)
        return event


class UserParticipantSerializer(serializers.ModelSerializer):
    user_participant = PresentablePrimaryKeyRelatedField(
        queryset=User.objects.all(),
        presentation_serializer=RegisterUserSerializer,
    )

    event_participant = PresentablePrimaryKeyRelatedField(
        queryset=Event.objects.all(),
        presentation_serializer=EventSerializer,
    )

    class Meta:
        model = UserParticipant
        fields = "__all__"


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = "__all__"
        
        # def create(self, request, validated_data):
        #     user_event_type = self.request.user.email
        #     event_type = EventType.objects.create(**validated_data)
            

class BookingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ["room_id", "time_from", "time_to"]

