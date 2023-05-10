from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager
from .managers import SellerManager
from .managers import UserManager

# Create your models here.


class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False)
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Auth User"
        verbose_name_plural = "Auth Users"


class User(CustomUser):
    objects = UserManager()

    class Meta:
        proxy = True


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Seller(CustomUser):
    objects = SellerManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_seller = True
        super().save(*args, **kwargs)


class SellerProfile(models.Model):
    user = models.OneToOneField(Seller, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
