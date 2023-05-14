from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager
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
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    address = models.ForeignKey("address.Address", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username
