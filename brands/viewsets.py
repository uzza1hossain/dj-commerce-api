from rest_framework import viewsets

from .models import Brand
from .permissions import IsBrandOwnerOrPublic
from .serializers import BrandSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsBrandOwnerOrPublic]
    lookup_field = "slug"

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_anonymous or not hasattr(user, "seller_profile"):  # type: ignore
            return Brand.objects.all()
        else:
            return Brand.objects.filter(owner=user.seller_profile) | Brand.objects.filter(is_public=True)  # type: ignore

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.seller_profile)  # type: ignore
