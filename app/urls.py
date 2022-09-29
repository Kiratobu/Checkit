from django.urls import path

from app.views import (
    BookingRoomView,
    BranchPostView,
    BranchView,
    BranchUpdateView,
    EventTypeUpdateView,
    EventTypeView,
    EventUpdateView,
    EventView,
    NotificationView,
    OrganisationView,
    PostView,
    PostUpdateView,
    RoomUpdateView,
    RoomView,
    UserParticipantUpdate,
    UserParticipantView,
    UserPostView,
)

urlpatterns = [
    path(
        "organisation/", OrganisationView.as_view(), name="create_organisation"
    ),
    path("post/", PostView.as_view(), name="create_post"),
    path("branchpost/", BranchPostView.as_view(), name="create_branch_post"),
    path("branch/", BranchView.as_view(), name="create_branch"),
    path("update_branch/<int:pk>", BranchUpdateView.as_view(),name="update_branch"),
    path("userpost/", UserPostView.as_view(), name="create_user_post"),
        path("update_post/<int:pk>", PostUpdateView.as_view(),name="update_post"),
    path("event/", EventView.as_view(), name="create_event"),
    path("event/<int:pk>/", EventUpdateView.as_view(), name="update_event"),
    path(
        "user_participant/",
        UserParticipantView.as_view(),
        name="create_participant",
    ),
    path(
        "user_participant/<int:pk>",
        UserParticipantUpdate.as_view(),
        name="update_user_part",
    ),
    path("event_type/", EventTypeView.as_view(), name="create_event_type"),
    path(
        "event_type/<int:pk>/",
        EventTypeUpdateView.as_view(),
        name="update_event_type",
    ),
    path("room/", RoomView.as_view(), name="create_room"),
    path("room/<int:pk>/", RoomUpdateView.as_view(), name="update_room"),
    path(
        "notification/", NotificationView.as_view(), name="create_notification"
    ),
    path(
        "booking_time/<int:pk>", BookingRoomView.as_view(), name="booking time"
    ),
]
