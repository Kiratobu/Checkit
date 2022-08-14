from urllib import request
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from app.permissions import CreatorPermission

# Create your views here.
from rest_framework.filters import SearchFilter

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
    permission_classes = [IsAdminUser]


class PostView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [IsAdminUser]


class BranchView(generics.ListCreateAPIView):
    serializer_class = BranchSerializer
    queryset = Branch.objects.all()
    permission_classes = [IsAdminUser]


class UserPostView(generics.ListCreateAPIView):
    serializer_class = UserPostSerializer
    queryset = UserPost.objects.all()
    filterset_fields = ["post"]
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )
    permission_classes = [IsAdminUser]


class BranchPostView(generics.ListCreateAPIView):
    serializer_class = BranchPostSerializer
    queryset = BranchPost.objects.all()
    filterset_fields = ["branch", "post"]
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )
    permission_classes = [IsAdminUser]


class EventView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Event.objects.filter(event_participant__user_participant=self.request.user.id)
        return queryset

class EventUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = Event.objects.filter(event_participant__user_participant=self.request.user.id)
        return queryset
    

class UserParticipantView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserParticipantSerializer
    queryset = UserParticipant.objects.all()


class UserParticipantUpdate(
    generics.RetrieveUpdateDestroyAPIView, CreatorPermission
):
    permission_classes = [IsAuthenticated]
    permission_classes = [CreatorPermission]
    serializer_class = UserParticipantSerializer
    queryset = UserParticipant.objects.all()


class EventTypeView(generics.ListCreateAPIView):
    serializer_class = EventTypeSerializer
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = EventType.objects.filter(user_event_type__id=self.request.user.id)
        return queryset
    
class EventTypeUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventTypeSerializer
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = EventType.objects.filter(user_event_type__id=self.request.user.id)
        return queryset


class RoomView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    
class RoomUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class NotificationView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
