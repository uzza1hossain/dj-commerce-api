# Generated by Django 4.2.1 on 2023-05-19 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("sellers", "0004_sellerprofile_profile_picture"),
        (
            "products",
            "0008_productattribute_owner_productattributevalue_owner_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="sellers.sellerprofile",
            ),
        ),
    ]