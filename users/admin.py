from django.contrib import admin

from .models import CustomUser
from .models import User
from .models import UserProfile

# Register your models here.


class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(User)
