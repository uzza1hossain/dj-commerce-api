# Generated by Django 4.2.1 on 2023-05-18 07:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("sellers", "0004_sellerprofile_profile_picture"),
    ]

    operations = [
        migrations.CreateModel(
            name="MediaAsset",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="media_assets",
                        to="sellers.sellerprofile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AssetFile",
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
                    "file",
                    models.FileField(
                        upload_to="media_assets/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=[
                                    ".png",
                                    ".jpg",
                                    ".jpeg",
                                    ".webp",
                                    ".mp4",
                                ],
                                message="Only PNG, JPG, JPEG, WEBP, and MP4 files are allowed.",
                            )
                        ],
                    ),
                ),
                ("alt_text", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "media_asset",
                    models.ManyToManyField(
                        related_name="files", to="media_assets.mediaasset"
                    ),
                ),
            ],
        ),
    ]
