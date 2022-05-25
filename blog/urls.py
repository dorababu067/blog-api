from django.urls import path
from .views import BlogEndpoint, BlogDetailEndpoint

urlpatterns = [
    path("blogs/", BlogEndpoint.as_view()),
    # blog detail endpoint this url will handle, retrieve, put, delete
    path("blogs/<int:id>/", BlogDetailEndpoint.as_view()),
]
