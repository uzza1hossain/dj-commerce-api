from media_assets.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework import viewsets

from .models import ProductAttribute
from .models import ProductAttributeThrough
from .models import ProductAttributeValue
from .serializers import ProductAttributeSerializer
from .serializers import ProductAttributeThroughSerializer
from .serializers import ProductAttributeValueSerializer


class ProductAttributeViewSet(viewsets.ModelViewSet):
    queryset = ProductAttribute.objects.all()
    serializer_class = ProductAttributeSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "seller_profile"):
            return ProductAttribute.objects.filter(owner=user.seller_profile)  # type: ignore
        return ProductAttribute.objects.all()


class ProductAttributeValueViewSet(viewsets.ModelViewSet):
    queryset = ProductAttributeValue.objects.all()
    serializer_class = ProductAttributeValueSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "seller_profile"):
            return ProductAttributeValue.objects.filter(owner=user.seller_profile)  # type: ignore
        return ProductAttributeValue.objects.none()


class ProductAttributeThroughViewSet(viewsets.ModelViewSet):
    queryset = ProductAttributeThrough.objects.all()
    serializer_class = ProductAttributeThroughSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ProductAttributeThrough.objects.filter(product__owner=self.request.user.seller_profile)  # type: ignore
        return ProductAttributeThrough.objects.all()
