from rest_framework import serializers

from .models import AssetFile
from .models import MediaAsset


class MediaAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaAsset
        fields = ["title", "description", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]


class AssetFileSerializer(serializers.ModelSerializer):
    media_asset = serializers.StringRelatedField(many=True)

    class Meta:
        model = AssetFile
        fields = ["file", "alt_text", "media_asset", "created_at", "updated_at"]
        read_only_fields = ["created_at", "updated_at"]

    def validate_media_asset(self, media_assets):
        user = self.context['request'].user
        if user.is_authenticated and hasattr(user, 'seller_profile'):
            for media_asset in media_assets:
                if media_asset.owner != user.seller_profile:
                    raise serializers.ValidationError("All media assets must be owned by the same seller.")
        return media_assets
