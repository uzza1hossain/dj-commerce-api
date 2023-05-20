from rest_framework import permissions

from .models import Brand


class IsBrandOwnerOrPublic(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Brand):
            if request.method in permissions.SAFE_METHODS:
                return True
            if (
                request.user.is_authenticated
                and obj.owner == request.user.seller_profile
            ):
                return request.method != "DELETE" or not obj.is_public
            if request.method == "DELETE" and obj.is_public:
                return request.user.is_staff or request.user.is_superuser
        return False
