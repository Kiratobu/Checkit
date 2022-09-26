from turtle import color
from urllib import request
import django_filters
from django_filters import DateFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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
from app.permissions import CreatorPermission
from app.serializers import (
    BookingRoomSerializer,
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
    filterset_fields = ["post", "user"]
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


class DateFilter(django_filters.FilterSet):
    start_date = DateFilter(
        field_name="date",
        lookup_expr=("gte"),
    )
    end_date = DateFilter(field_name="date", lookup_expr=("lte"))

    class Meta:
        model = Event
        fields = ["title", "date"]


class EventView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    filter_class = DateFilter
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )

    def get_queryset(self):
        queryset = Event.objects.filter(
            event_participant__user_participant=self.request.user.id
        )
        return queryset


class EventUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.filter(
            event_participant__user_participant=self.request.user.id
        )
        return queryset


class UserParticipantView(generics.ListCreateAPIView):
    serializer_class = UserParticipantSerializer
    queryset = UserParticipant.objects.all()


class UserParticipantUpdate(
    generics.RetrieveUpdateDestroyAPIView, CreatorPermission
):
    permission_classes = [CreatorPermission]
    serializer_class = UserParticipantSerializer
    queryset = UserParticipant.objects.all()


class EventTypeView(generics.ListCreateAPIView):
    serializer_class = EventTypeSerializer
    # permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = EventType.objects.filter(
            user_event_type__id=self.request.user.id
        )
        return queryset
    
    def get_serializer_context(self):
        context = super(EventTypeView, self).get_serializer_context()
        context.update({"request_user_id": self.request.user.id})
        print(context)
        return context
    
        


class EventTypeUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventTypeSerializer
    
    def get_queryset(self):
        queryset = EventType.objects.filter(
            user_event_type__id=self.request.user.id
        )
        return queryset


class RoomView(generics.ListCreateAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class RoomUpdateView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAdminUser]
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    filterset_fields = ["title", "description", "capacity"]
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )


class NotificationView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()


class BookingRoomView(APIView):
    def get(self, request, pk):
        serializer = BookingRoomSerializer(
            Event.objects.filter(room_id__id=pk), many=True
        )
        return Response({"booking time": serializer.data})
