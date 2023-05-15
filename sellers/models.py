from address.models import Address
from django.contrib.contenttypes.models import ContentType
from django.db import models
from sellers.managers import SellerManager
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.placeholder import OnStoragePlaceholderImage

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
    profile_picture = VersatileImageField(
        upload_to="seller_profile_pictures",
        blank=True,
        null=True,
        placeholder_image=OnStoragePlaceholderImage(  # type: ignore
            path="images/default_profile_pic.jpg"
        ),
    )

    def __str__(self):
        return self.user.username

    def get_addresses(self):
        content_type = ContentType.objects.get_for_model(self)
        return Address.objects.filter(content_type=content_type, object_id=self.id)  # type: ignore
