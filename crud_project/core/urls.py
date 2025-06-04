from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import CredentialViewSet, InstitutionViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'credentials', CredentialViewSet)
router.register(r'institutions', InstitutionViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
