from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser
from .models import User
from .models import UserProfile
from sellers.models import Seller
from sellers.models import SellerProfile


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created and not instance.is_seller and not instance.is_superuser:
        UserProfile.objects.create(user=instance)
    if created and instance.is_seller:
        SellerProfile.objects.create(user=instance)
