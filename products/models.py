from decimal import Decimal

from brands.models import Brand
from categories.models import Category
from django.core.validators import MinValueValidator
from django.db import models
from media_assets.models import MediaAsset
from sellers.models import Seller
from sellers.models import SellerProfile


class ProductAttribute(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProductAttributeValue(models.Model):
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.value


class Product(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    sku = models.CharField(max_length=80, unique=True)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(SellerProfile, on_delete=models.CASCADE)
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
    store_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    is_digital = models.BooleanField(
        default=False,
    )
    weight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    attributes = models.ManyToManyField(
        ProductAttributeValue, through="VariantAttributeThrough"
    )
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.product} - Attributes: {self.attributes} - Stock: {self.stock}"

    def remove_stock(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            self.save()
        else:
            raise ValueError("Insufficient stock")


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
