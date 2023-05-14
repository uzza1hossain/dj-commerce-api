# Generated by Django 4.2.1 on 2023-05-14 03:37

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import smart_selects.db_fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("name", models.CharField(max_length=255)),
                ("code", models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name="State",
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
                ("name", models.CharField(max_length=255)),
                ("code", models.CharField(max_length=5)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="address.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
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
                ("street_address", models.CharField(max_length=255)),
                ("apt", models.CharField(blank=True, max_length=50, null=True)),
                ("city", models.CharField(max_length=50)),
                ("zip_code", models.CharField(max_length=10)),
                (
                    "phone_number",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, region=None
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="address.country",
                    ),
                ),
                (
                    "state",
                    smart_selects.db_fields.ChainedForeignKey(
                        auto_choose=True,
                        chained_field="country",
                        chained_model_field="country",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="address.state",
                    ),
                ),
            ],
        ),
    ]
