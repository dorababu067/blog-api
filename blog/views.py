from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from .models import Blog
from .serializers import BlogSerializer


class BlogEndpoint(ListAPIView, CreateAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class BlogDetailEndpoint(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    lookup_field = "id"
