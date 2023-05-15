from rest_framework.permissions import BasePermission


class IsUserOrSeller(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            hasattr(request.user, "user_profile")
            or hasattr(request.user, "seller_profile")
        )

    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, "user_profile"):
            return request.user.user_profile == obj.associated_profile
        elif hasattr(request.user, "seller_profile"):
            return request.user.seller_profile == obj.associated_profile
        return False
