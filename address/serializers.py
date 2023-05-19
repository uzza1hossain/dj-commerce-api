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
            state_name = state_name.strip().capitalize()
            queryset = State.objects.filter(name=state_name)
        else:
            queryset = State.objects.none()
        return queryset

    def to_internal_value(self, data):
        state_name = data.strip().capitalize()
        if state_name:
            state = State.objects.filter(name=state_name).first()
            if state:
                return state
            raise serializers.ValidationError("Invalid state name")

    def to_representation(self, value):
        return value.name


class CountryName(serializers.SlugRelatedField):
    def get_queryset(self):
        country_name = self.context["request"].data.get("country")
        if country_name:
            country_name = country_name.strip().capitalize()
            queryset = Country.objects.filter(name=country_name)
        else:
            queryset = Country.objects.none()
        return queryset

    def to_internal_value(self, data):
        country_name = data.strip().capitalize()
        if country_name:
            country = Country.objects.filter(name=country_name).first()
            if country:
                return country
            raise serializers.ValidationError("Invalid country name")

    def to_representation(self, value):
        return value.name


class AddressSerializer(serializers.ModelSerializer):
    state = StateName(slug_field="name")
    country = CountryName(slug_field="name")
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
            country = Country.objects.get(name=country_name.strip().capitalize())
        except Country.DoesNotExist:
            raise serializers.ValidationError("Invalid country")

        zip_code_regex = country.zipcode_regex
        if not re.match(zip_code_regex, value):  # type: ignore
            raise serializers.ValidationError("Invalid zip code")

        return value
