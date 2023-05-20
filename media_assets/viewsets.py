from rest_framework import viewsets

from .models import AssetFile
from .models import MediaAsset
from .permissions import IsOwnerOrReadOnly
from .serializers import AssetFileSerializer
from .serializers import MediaAssetSerializer


class MediaAssetViewSet(viewsets.ModelViewSet):
    queryset = MediaAsset.objects.all()
    serializer_class = MediaAssetSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "seller_profile"):
            return MediaAsset.objects.filter(owner=user.seller_profile)  # type: ignore
        else:
            return MediaAsset.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.seller_profile)  # type: ignore


class AssetFileViewSet(viewsets.ModelViewSet):
    queryset = AssetFile.objects.all()
    serializer_class = AssetFileSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and hasattr(user, "seller_profile"):
            return AssetFile.objects.filter(owner=user.seller_profile)  # type: ignore
        else:
            return AssetFile.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.seller_profile)  # type: ignore
