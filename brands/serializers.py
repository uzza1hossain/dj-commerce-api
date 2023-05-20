from rest_framework import serializers

from .models import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'slug', 'description', 'assets', 'created_at', 'updated_at', 'owner', 'is_public']

    def validate_is_public(self, value):
        if self.instance and self.instance.is_public:
            raise serializers.ValidationError("Cannot change a brand from public to private.")
        return value
