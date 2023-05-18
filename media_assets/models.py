from django.core.validators import FileExtensionValidator
from django.db import models
from sellers.models import SellerProfile


class MediaAsset(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(
        SellerProfile,
        on_delete=models.CASCADE,
        related_name="media_assets",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class AssetFile(models.Model):
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
    media_asset = models.ManyToManyField(
        MediaAsset,
        related_name="files",
    )

    def __str__(self):
        return self.file.name
