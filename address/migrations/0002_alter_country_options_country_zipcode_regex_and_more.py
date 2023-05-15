# Generated by Django 4.2.1 on 2023-05-14 04:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("address", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="country",
            options={"verbose_name": "Country", "verbose_name_plural": "Countries"},
        ),
        migrations.AddField(
            model_name="country",
            name="zipcode_regex",
            field=models.CharField(default="BD", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="country",
            name="code",
            field=models.CharField(max_length=2),
        ),
    ]