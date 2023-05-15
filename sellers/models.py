from address.models import Address
from django.contrib.contenttypes.models import ContentType
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
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="seller_profile"
    )

    def __str__(self):
        return self.user.username

    def get_addresses(self):
        content_type = ContentType.objects.get_for_model(self)
        return Address.objects.filter(content_type=content_type, object_id=self.id)  # type: ignore
