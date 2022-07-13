from django.shortcuts import render
from rest_framework import generics
from app.serializers import OrganisationSerializer, PostSerializer, BranchSerializer, UserPostSerializer, BranchPostSerializer
from app.models import Organisation, Post, Branch, UserPost, BranchPost
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