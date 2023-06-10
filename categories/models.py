from core.mixins import SlugMixin
from core.models import BaseModel
from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey


# Create your models here.
class Category(SlugMixin, MPTTModel):
    name = models.CharField(
        max_length=100,
    )
    slug = models.SlugField(max_length=150, unique=True)
    is_active = models.BooleanField(
        default=False,
    )
    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        ordering = ["name"]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("categories-detail", kwargs={"slug": self.slug})
