from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Blog
from .serializers import BlogSerializer

# C - CREATE    --> Method POST
# R - GET (All)  --> Method GET

# R - RETRIEVE(Single)  --> Method GET -- id
# U - UPDATE    --> Method PUT -- id
# D - DELETE    --> Method DELETE -- id


@api_view(["GET", "POST"])
def blog_endpoint(request):
    """This endpoint will handle GET, POST methods"""

    if request.method == "GET":
        # queryset will return all objects inside the blog table
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def blog_detail_endpoint(request, id):
    """This endpoint  will handle RETRIEVE, UPDATE, DELETE methods"""

    # get individual blog
    try:
        blog = Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404

    # RETRIEVE BLOG will only one object data
    if request.method == "GET":
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    if request.method == "PUT":
        # Update the
        serializer = BlogSerializer(instance=blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
