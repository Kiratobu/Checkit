from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.permissions import SAFE_METHODS, BasePermission

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

# Create your views here.
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


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
    filterset_fields = ["post"]
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )
    
class BranchPostView(generics.ListCreateAPIView):
    serializer_class = BranchPostSerializer
    queryset = BranchPost.objects.all()
    filterset_fields = [ "branch", "post"]
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )


class EventView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()


class PostUserWritePermission(BasePermission):
    message = 'Editing event is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.user_participant == request.user

class UserParticipantView(generics.ListCreateAPIView):
    serializer_class = UserParticipantSerializer
    queryset = UserParticipant.objects.all()
    

class UserParticipantUpdate(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
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
