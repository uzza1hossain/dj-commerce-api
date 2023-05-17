from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey


# Create your models here.
class Category(MPTTModel):
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
        return reverse("category_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
