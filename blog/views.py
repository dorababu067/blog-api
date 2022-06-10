from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

from .models import Blog
from django.contrib.auth.models import User

from .serializers import BlogSerializer, UserSerializer


class BlogEndpoint(ListAPIView, CreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = [IsAuthenticated]


class BlogDetailEndpoint(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field = "id"
    permission_classes = [IsAuthenticated]


class UserRegisterEndpoint(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(self.request.data.get("password"))
            # crete new user
            user.save()
