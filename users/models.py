from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import SellerManager

# Create your models here.


class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


class Seller(CustomUser):
    objects = SellerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_seller = True
        super().save(*args, **kwargs)


class SellerProfile(models.Model):
    user = models.OneToOneField(Seller, on_delete=models.CASCADE)
