from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()
    is_active = serializers.BooleanField()

    class Meta:
        model = Category
        fields = ["id", "name", "slug", "is_active", "parent", "children"]
        read_only_fields = ["id", "slug", "is_active"]

    def get_children(self, obj) -> list:
        serializer = self.__class__(obj.children.all(), many=True)
        return serializer.data # type: ignore
