from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Category
from .permissions import CategoryPermissions
from .serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [CategoryPermissions]
    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "toggle_active":
            return serializers.Serializer
        return super().get_serializer_class()

    @action(
        detail=True,
        methods=["patch"],
        url_path="toggle-active",
    )
    def toggle_active(self, request, slug=None):
        category = self.get_object()
        category.is_active = not category.is_active
        category.save()

        return Response({"detail": "Toggle successful."})
