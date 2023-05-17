from rest_framework import permissions


class CategoryPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ["list", "retrieve"]:
            return True
        elif view.action in ["create", "update"]:
            return request.user.is_authenticated and (
                request.user.is_seller
                or request.user.is_superuser
                or request.user.is_staff
            )
        elif view.action in ["destroy", "toggle_active"]:
            return request.user.is_superuser or request.user.is_staff
        return False

    def has_object_permission(self, request, view, obj):
        if view.action in ["retrieve"]:
            return True
        elif view.action == "update":
            return request.user.is_authenticated and (
                request.user.is_seller
                or request.user.is_superuser
                or request.user.is_staff
            )
        elif view.action in ["destroy", "toggle_active"]:
            return request.user.is_staff or request.user.is_superuser
        return False
