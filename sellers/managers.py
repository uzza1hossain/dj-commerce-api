from users.managers import CustomUserManager


class SellerManager(CustomUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_seller=True)
