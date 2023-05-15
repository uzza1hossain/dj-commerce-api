from address.models import Address
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models
from versatileimagefield.fields import VersatileImageField
from versatileimagefield.placeholder import OnStoragePlaceholderImage

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
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="user_profile"
    )
    profile_picture = VersatileImageField(upload_to="user_profile_pictures", blank=True, null=True, placeholder_image=OnStoragePlaceholderImage(  # type: ignore
            path='images/default_profile_pic.jpg'
        ))

    def __str__(self):
        return self.user.username

    def get_addresses(self):
        content_type = ContentType.objects.get_for_model(self)
        return Address.objects.filter(content_type=content_type, object_id=self.id)  # type: ignore
