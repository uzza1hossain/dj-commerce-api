from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser
from .models import Seller
from .models import SellerProfile
from .models import UserProfile


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=Seller)
def create_seller_profile(sender, instance, created, **kwargs):
    if created:
        SellerProfile.objects.create(user=instance)
