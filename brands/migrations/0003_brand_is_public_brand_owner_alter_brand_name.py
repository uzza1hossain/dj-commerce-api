# Generated by Django 4.2.1 on 2023-05-20 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_alter_customuser_managers"),
        ("brands", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="brand",
            name="is_public",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="brand",
            name="owner",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="brands",
                to="users.sellerprofile",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="brand",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
