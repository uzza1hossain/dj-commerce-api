from django.urls import path
from rest_framework import routers

from .viewsets import AssetFileViewSet
from .viewsets import MediaAssetViewSet


router = routers.DefaultRouter()
router.register(r"media-assets", MediaAssetViewSet, basename="media_assets")
router.register(r"asset-files", AssetFileViewSet, basename="asset_files")

urlpatterns = router.urls
