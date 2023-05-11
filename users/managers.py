from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    pass


class UserManager(CustomUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_seller=False).filter(is_superuser=False)



