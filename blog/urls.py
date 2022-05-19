from django.urls import path
from .views import blog_endpoint, blog_detail_endpoint


urlpatterns = [
    path("blogs/", blog_endpoint),
    # blog detail endpoint this url will handle, retrieve, put, delete
    path("blogs/<int:id>/", blog_detail_endpoint),
]
