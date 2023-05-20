from address.models import Address
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django_lifecycle import AFTER_CREATE
from django_lifecycle import hook
from django_lifecycle import LifecycleModel
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.placeholder import OnStoragePlaceholderImage

from .managers import CustomUserManager
from .managers import SellerManager
from .managers import UserManager

# Create your models here.


class CustomUser(AbstractUser):
    is_seller = models.BooleanField(default=False)
    objects = CustomUserManager()
    users = UserManager()
    sellers = SellerManager()

    def __str__(self):
        return self.username

    def get_user_profile(self):
        if hasattr(self, "user_profile"):
            return self.user_profile  # type: ignore
        return None

    def get_seller_profile(self):
        if hasattr(self, "seller_profile"):
            return self.seller_profile  # type: ignore
        return None

    def get_profile(self):
        if hasattr(self, "user_profile"):
            return "user", self.user_profile  # type: ignore
        elif hasattr(self, "seller_profile"):
            return "seller", self.seller_profile  # type: ignore
        else:
            return None, None

    @hook(AFTER_CREATE)
    def create_profile(self):
        if self.is_seller:
            SellerProfile.objects.create(user=self)
        elif not self.is_superuser:
            UserProfile.objects.create(user=self)


class UserProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="user_profile"
    )
    profile_picture = VersatileImageField(
        upload_to="user_profile_pictures",
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
