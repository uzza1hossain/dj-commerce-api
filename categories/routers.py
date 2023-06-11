from rest_framework import routers
from django.urls import path
from .viewsets import CategoryViewSet

router = routers.SimpleRouter()
router.register(r"", CategoryViewSet, basename="categories")

