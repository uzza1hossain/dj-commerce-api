from rest_framework import exceptions
from rest_framework import serializers

from .models import ProductAttribute
from .models import ProductAttributeThrough
from .models import ProductAttributeValue


class ProductAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttribute
        fields = "__all__"

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user.seller_profile
        return super().create(validated_data)

    # def update(self, instance, validated_data):
    #     validated_data["owner"] = self.context["request"].user.seller_profile
    #     return super().update(instance, validated_data)


class ProductAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeValue
        fields = "__all__"

    def create(self, validated_data):
        attribute = validated_data.get("attribute")
        owner = self.context["request"].user.seller_profile

        # Check if the owner of the ProductAttribute is the same as the current user
        if attribute.owner != owner:
            raise exceptions.PermissionDenied(
                "The referenced attribute must be owned by the same user"
            )

        validated_data["owner"] = owner
        return super().create(validated_data)

    def update(self, instance, validated_data):
        attribute = validated_data.get("attribute")
        owner = self.context["request"].user.seller_profile

        # Check if the owner of the ProductAttribute is the same as the current user
        if attribute and attribute.owner != owner:
            raise exceptions.PermissionDenied(
                "The referenced attribute must be owned by the same user"
            )

        return super().update(instance, validated_data)


class ProductAttributeThroughSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAttributeThrough
        fields = "__all__"

    def create(self, validated_data):
        product = validated_data.get("product")
        attribute = validated_data.get("attribute")
        value = validated_data.get("value")
        owner = self.context["request"].user.seller_profile

        # Check if the owner of the Product, ProductAttribute and ProductAttributeValue is the same as the current user
        if product.owner != owner or attribute.owner != owner or value.owner != owner:
            raise exceptions.PermissionDenied(
                "The referenced product, attribute, and value must be owned by the same user"
            )

        return super().create(validated_data)

    def update(self, instance, validated_data):
        product = validated_data.get("product")
        attribute = validated_data.get("attribute")
        value = validated_data.get("value")
        owner = self.context["request"].user.seller_profile

        # Check if the owner of the Product, ProductAttribute and ProductAttributeValue is the same as the current user
        if (
            (product and product.owner != owner)
            or (attribute and attribute.owner != owner)
            or (value and value.owner != owner)
        ):
            raise exceptions.PermissionDenied(
                "The referenced product, attribute, and value must be owned by the same user"
            )

        return super().update(instance, validated_data)
