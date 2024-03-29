from decimal import Decimal

from brands.models import Brand
from categories.models import Category
from core.mixins import SlugMixin
from core.models import BaseModel
from django.core.validators import MinValueValidator
from django.db import models
from django_lifecycle import AFTER_DELETE
from django_lifecycle import AFTER_SAVE
from django_lifecycle import BEFORE_SAVE
from django_lifecycle import hook
from django_lifecycle import LifecycleModel
from media_assets.models import MediaAsset

from users.models import SellerProfile


class ProductAttribute(models.Model):
    owner = models.ForeignKey(
        SellerProfile, on_delete=models.CASCADE, related_name="product_attributes"
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProductAttributeValue(models.Model):
    owner = models.ForeignKey(
        SellerProfile, on_delete=models.CASCADE, related_name="product_attribute_values"
    )
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.value


class Product(LifecycleModel, SlugMixin, BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    sku = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(
        SellerProfile, on_delete=models.CASCADE, related_name="products"
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True
    )
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    assets = models.ForeignKey(
        MediaAsset, on_delete=models.SET_NULL, null=True, blank=True
    )
    attributes = models.ManyToManyField(
        ProductAttribute, through="ProductAttributeThrough"
    )
    is_active = models.BooleanField(default=False)
    retail_price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.01"))]
    )
    store_price = models.DecimalField(max_digits=5, decimal_places=2)
    is_digital = models.BooleanField(default=False)
    weight = models.FloatField()
    stock = models.PositiveIntegerField(default=0, editable=False)

    @hook(AFTER_SAVE, when="product_variants__stock", has_changed=True)
    @hook(AFTER_DELETE, when="product_variants")
    def update_stock(self):
        self.stock = sum(variant.stock for variant in self.product_variants.all())  # type: ignore
        self.save()


class ProductVariant(LifecycleModel, SlugMixin, BaseModel):
    owner = models.ForeignKey(
        SellerProfile, on_delete=models.CASCADE, related_name="product_variants"
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    sku = models.CharField(max_length=80, unique=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_variants"
    )
    attributes = models.ManyToManyField(
        ProductAttributeValue, through="VariantAttributeThrough"
    )
    stock = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=False)

    @hook(BEFORE_SAVE, when="stock", has_changed=True)
    def update_product_stock(self):
        self.product.update_stock()

    def remove_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()
        else:
            raise ValueError("Insufficient stock")

    def add_stock(self, quantity):
        self.stock += quantity
        self.save()


class VariantAttributeThrough(models.Model):
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE)
    attribute_value = models.ForeignKey(ProductAttributeValue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.variant} - Attribute Value: {self.attribute_value}"


class ProductAttributeThrough(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    value = models.ForeignKey(ProductAttributeValue, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product} - {self.attribute}: {self.value}"
