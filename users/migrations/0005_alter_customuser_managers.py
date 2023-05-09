# Generated by Django 4.2.1 on 2023-05-09 05:23

from django.db import migrations
import users.managers


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_alter_customuser_options"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="customuser",
            managers=[
                ("objects", users.managers.CustomUserManager()),
            ],
        ),
    ]
