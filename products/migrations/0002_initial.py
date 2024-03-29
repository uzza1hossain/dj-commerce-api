# Generated by Django 4.2.1 on 2023-05-22 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("media_assets", "0002_initial"),
        ("brands", "0003_initial"),
        ("categories", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="productvariant",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_variants",
                to="users.sellerprofile",
            ),
        ),
        migrations.AddField(
            model_name="productvariant",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_variants",
                to="products.product",
            ),
        ),
        migrations.AddField(
            model_name="productattributevalue",
            name="attribute",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="products.productattribute",
            ),
        ),
        migrations.AddField(
            model_name="productattributevalue",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_attribute_values",
                to="users.sellerprofile",
            ),
        ),
        migrations.AddField(
            model_name="productattributethrough",
            name="attribute",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="products.productattribute",
            ),
        ),
        migrations.AddField(
            model_name="productattributethrough",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="products.product"
            ),
        ),
        migrations.AddField(
            model_name="productattributethrough",
            name="value",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="products.productattributevalue",
            ),
        ),
        migrations.AddField(
            model_name="productattribute",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product_attributes",
                to="users.sellerprofile",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="assets",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="media_assets.mediaasset",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="attributes",
            field=models.ManyToManyField(
                through="products.ProductAttributeThrough",
                to="products.productattribute",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="brands.brand",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="categories.category",
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="users.sellerprofile",
            ),
        ),
    ]
