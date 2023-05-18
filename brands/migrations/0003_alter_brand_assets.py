# Generated by Django 4.2.1 on 2023-05-18 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("media_assets", "0001_initial"),
        ("brands", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brand",
            name="assets",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="brand",
                to="media_assets.mediaasset",
            ),
        ),
    ]