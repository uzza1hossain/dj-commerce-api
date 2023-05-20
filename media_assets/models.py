from core.models import BaseModel
from django.core.validators import FileExtensionValidator
from django.db import models

from users.models import SellerProfile


class MediaAsset(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(
        SellerProfile,
        on_delete=models.CASCADE,
        related_name="media_assets",
    )

    def __str__(self):
        return self.title


class AssetFile(BaseModel):
    IMAGE_EXTENSIONS = ["png", "jpg", "jpeg", "webp"]
    VIDEO_EXTENSIONS = ["mp4"]
    file = models.FileField(
        upload_to="media_assets/",
        validators=[
            FileExtensionValidator(
                allowed_extensions=IMAGE_EXTENSIONS + VIDEO_EXTENSIONS,
                message="Only PNG, JPG, JPEG, WEBP, and MP4 files are allowed.",
            )
        ],
    )
    alt_text = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(
        SellerProfile, on_delete=models.CASCADE, related_name="media_files"
    )
    media_asset = models.ManyToManyField(
        MediaAsset,
        related_name="files",
    )

    def __str__(self):
        return self.file.name
