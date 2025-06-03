from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import register_user, protected_view

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),   # login endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # refresh token endpoint
    path('protected/', protected_view, name='protected'),

]
