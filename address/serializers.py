import re

from rest_framework import serializers

from .models import Address
from .models import Country
from .models import State


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ["name"]


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["name"]


class StateName(serializers.SlugRelatedField):
    def get_queryset(self):
        state_name = self.context["request"].data.get("state")
        if state_name:
            queryset = State.objects.filter(name=state_name)
        else:
            queryset = State.objects.none()
        return queryset

    def to_internal_value(self, data):
        state_name = data
        if state_name:
            state = State.objects.filter(name=state_name).first()
            if state:
                return state
        raise serializers.ValidationError("Invalid state name")

    def to_representation(self, value):
        return value.name


class AddressSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    country = serializers.SlugRelatedField(
        queryset=Country.objects.all(), slug_field="name"
    )
    state = StateName(queryset=State.objects.all(), slug_field="name")
    zip_code = serializers.CharField(max_length=10)

    class Meta:
        model = Address
        fields = [
            "id",
            "street_address",
            "apt",
            "city",
            "zip_code",
            "phone_number",
            "country",
            "state",
        ]

    def validate_zip_code(self, value):
        country_name = self.initial_data.get("country")  # type: ignore
        try:
            country = Country.objects.get(name=country_name)
        except Country.DoesNotExist:
            raise serializers.ValidationError("Invalid country")

        zip_code_regex = country.zipcode_regex
        if not re.match(zip_code_regex, value):
            raise serializers.ValidationError("Invalid zip code")

        return value
