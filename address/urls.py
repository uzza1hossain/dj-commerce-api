from django.urls import include
from django.urls import path
from rest_framework import routers

from .views import AddressViewSet

router = routers.DefaultRouter()
router.register(r"addresses", AddressViewSet)

urlpatterns = [
    # Other URL patterns
    path("", include(router.urls)),
]
