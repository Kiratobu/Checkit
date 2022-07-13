from rest_framework import generics

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
from app.serializers import (
    BranchPostSerializer,
    BranchSerializer,
    EventSerializer,
    EventTypeSerializer,
    NotificationSerializer,
    OrganisationSerializer,
    PostSerializer,
    RoomSerializer,
    UserParticipantSerializer,
    UserPostSerializer,
)

class OrganisationView(generics.ListCreateAPIView):
    serializer_class = OrganisationSerializer
    queryset = Organisation.objects.all()


class PostView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class BranchView(generics.ListCreateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()


class UserPostView(generics.ListCreateAPIView):
    serializer_class = UserPostSerializer
    queryset = UserPost.objects.all()


class BranchPostView(generics.ListCreateAPIView):
    serializer_class = BranchPostSerializer
    queryset = BranchPost.objects.all()


class EventView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class UserParticipantView(generics.ListCreateAPIView):
    serializer_class = UserParticipantSerializer
    queryset = UserParticipant.objects.all()


class EventTypeView(generics.ListCreateAPIView):
    serializer_class = EventTypeSerializer
    queryset = EventType.objects.all()


class RoomView(generics.ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class NotificationView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
