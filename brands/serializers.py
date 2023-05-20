from rest_framework import serializers

from .models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = [
            "name",
            "slug",
            "description",
            "assets",
            "created_at",
            "updated_at",
            "is_public",
        ]
        read_only_fields = ["slug", "created_at", "updated_at"]

    def validate_is_public(self, value):
        if self.instance and self.instance.is_public:
            raise serializers.ValidationError(
                "Cannot change a brand from public to private."
            )
        return value
