from django.urls import path
from .views import (
    BlogEndpoint,
    BlogDetailEndpoint,
    UserRegisterEndpoint,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path("blogs/", BlogEndpoint.as_view()),
    # blog detail endpoint this url will handle, retrieve, put, delete
    path("blogs/<int:id>/", BlogDetailEndpoint.as_view()),
    path("register/", UserRegisterEndpoint.as_view()),
    # JWTAuthentication
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
