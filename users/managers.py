from django.contrib.auth.models import UserManager # type: ignore


class CustomUserManager(UserManager):
    pass


class UserManager(CustomUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_seller=False).filter(is_superuser=False)


class SellerManager(CustomUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_seller=True)
