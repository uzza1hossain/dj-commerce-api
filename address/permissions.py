from rest_framework.permissions import BasePermission


class IsUserOrSeller(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            hasattr(request.user, "user_profile")
            or hasattr(request.user, "seller_profile")
        )

    def has_object_permission(self, request, view, obj):
        return obj.associated_profile in [
            request.user.user_profile,
            request.user.seller_profile,
        ]
