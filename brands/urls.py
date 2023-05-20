from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import BrandViewSet

router = DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brand')

urlpatterns = router.urls
