from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from .viewsets import ProductAttributeThroughViewSet
from .viewsets import ProductAttributeValueViewSet
from .viewsets import ProductAttributeViewSet

router = DefaultRouter()
router.register(
    r"product-attributes", ProductAttributeViewSet, basename="product-attributes"
)
router.register(
    r"product-attribute-values",
    ProductAttributeValueViewSet,
    basename="product-attribute-values",
)
router.register(
    r"product-attribute-throughs",
    ProductAttributeThroughViewSet,
    basename="product-attribute-throughs",
)

urlpatterns = router.urls
