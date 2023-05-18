# Generated by Django 4.2.1 on 2023-05-17 18:13

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("web_id", models.CharField(max_length=50, unique=True)),
                ("slug", models.SlugField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("is_active", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="product",
                        to="categories.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductAttribute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProductAttributeValue",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("attribute_value", models.CharField(max_length=255)),
                (
                    "product_attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_attribute",
                        to="products.productattribute",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductAttributeValues",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "attributevalues",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="attributevaluess",
                        to="products.productattributevalue",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductInventory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sku", models.CharField(max_length=20, unique=True)),
                ("upc", models.CharField(max_length=12, unique=True)),
                ("is_active", models.BooleanField(default=False)),
                ("is_default", models.BooleanField(default=False)),
                (
                    "retail_price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=10,
                        validators=[
                            django.core.validators.MinValueValidator(Decimal("0.01"))
                        ],
                    ),
                ),
                ("store_price", models.DecimalField(decimal_places=2, max_digits=5)),
                ("is_digital", models.BooleanField(default=False)),
                ("weight", models.FloatField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "attribute_values",
                    models.ManyToManyField(
                        related_name="product_attribute_values",
                        through="products.ProductAttributeValues",
                        to="products.productattributevalue",
                    ),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="brand",
                        to="products.brand",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product",
                        to="products.product",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("last_checked", models.DateTimeField(blank=True, null=True)),
                ("units", models.IntegerField(default=0)),
                ("units_sold", models.IntegerField(default=0)),
                (
                    "product_inventory",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="product_inventory",
                        to="products.productinventory",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductTypeAttribute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product_attribute",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="productattribute",
                        to="products.productattribute",
                    ),
                ),
                (
                    "product_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="producttype",
                        to="products.producttype",
                    ),
                ),
            ],
            options={
                "unique_together": {("product_attribute", "product_type")},
            },
        ),
        migrations.AddField(
            model_name="producttype",
            name="product_type_attributes",
            field=models.ManyToManyField(
                related_name="product_type_attributes",
                through="products.ProductTypeAttribute",
                to="products.productattribute",
            ),
        ),
        migrations.AddField(
            model_name="productinventory",
            name="product_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="product_type",
                to="products.producttype",
            ),
        ),
        migrations.AddField(
            model_name="productattributevalues",
            name="productinventory",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="productattributevaluess",
                to="products.productinventory",
            ),
        ),
        migrations.CreateModel(
            name="Media",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("img_url", models.ImageField(upload_to="")),
                ("alt_text", models.CharField(max_length=255)),
                ("is_feature", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product_inventory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="media",
                        to="products.productinventory",
                    ),
                ),
            ],
        ),
        migrations.AlterUniqueTogether(
            name="productattributevalues",
            unique_together={("attributevalues", "productinventory")},
        ),
    ]
