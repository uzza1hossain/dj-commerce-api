from django.db import models
from sellers.managers import SellerManager

from users.models import CustomUser


# Create your models here.
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
