from ast import Delete
from django.http import Http404


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Blog
from .serializers import BlogSerializer


class BlogEndpoint(APIView):
    def get(self, request):
        # queryset will return all objects inside the blog table
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailEndpoint(APIView):
    def get_blog(self, id):
        try:
            blog = Blog.objects.get(id=id)
            return blog
        except Blog.DoesNotExist:
            raise Http404

    # get individual blog
    def get(self, request, id):
        blog = self.get_blog(id)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    def put(self, request, id):
        blog = self.get_blog(id)

        # Update the
        serializer = BlogSerializer(instance=blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        blog = self.get_blog(id)

        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
