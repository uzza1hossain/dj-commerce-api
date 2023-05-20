from core.mixins import SlugMixin
from core.models import BaseModel
from django.db import models
from media_assets.models import MediaAsset

from users.models import SellerProfile


# Create your models here.
class Brand(SlugMixin, BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(
        SellerProfile, on_delete=models.CASCADE, related_name="brands"
    )
    assets = models.ForeignKey(
        MediaAsset,
        on_delete=models.SET_NULL,
        related_name="brand",
        null=True,
        blank=True,
    )
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.name
