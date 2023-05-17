from rest_framework import routers

from .viewsets import CategoryViewSet

router = routers.SimpleRouter()
router.register(r"", CategoryViewSet, basename="categories")
