from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
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
    BookingRoomSerializer,
)

# Create your views here.
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import DateFilter
import django_filters

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

class DateFilter(django_filters.FilterSet):
    start_date=DateFilter(field_name='date', lookup_expr=('gte'),)
    end_date=DateFilter(field_name='date', lookup_expr=('lte'))
    class Meta:
        model = Event
        fields = ['title', 'date']

class EventView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    filter_class = DateFilter
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )

class UserParticipantView(generics.ListCreateAPIView):
    serializer_class = UserParticipantSerializer
    queryset = UserParticipant.objects.all()


class EventTypeView(generics.ListCreateAPIView):
    serializer_class = EventTypeSerializer
    queryset = EventType.objects.all()


class RoomView(generics.ListCreateAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    filterset_fields = [ "title", "description", "capacity"]
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
    )

class NotificationView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()

class BookingRoomView(APIView):
    def get(self, request, pk):
        serializer = BookingRoomSerializer(Event.objects.filter(room_id__id=pk), many = True)
        return Response({"booking time" : serializer.data})