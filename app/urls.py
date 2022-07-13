from django.urls import path
from app.views import (
    BranchPostView,
    BranchView,
    EventTypeView,
    EventView,
    NotificationView,
    OrganisationView,
    PostView,
    RoomView,
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
    path("userpost/", UserPostView.as_view(), name="create_user_post"),
    path("event/", EventView.as_view(), name="create_event"),
    path(
        "user_participant/",
        UserParticipantView.as_view(),
        name="create_participant",
    ),
    path("event_type/", EventTypeView.as_view(), name="create_event_type"),
    path("room/", RoomView.as_view(), name="create_room"),
    path(
        "notification/", NotificationView.as_view(), name="create_notification"
    ),
]