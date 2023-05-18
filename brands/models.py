from django.db import models
from media_assets.models import MediaAsset
from versatileimagefield.fields import VersatileImageField


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    assets = models.OneToOneField(
        MediaAsset,
        on_delete=models.SET_NULL,
        related_name="brand",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
