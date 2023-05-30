import re

from phonenumber_field.phonenumber import PhoneNumber
from phonenumber_field.serializerfields import PhoneNumberField
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
            state_name = state_name.strip().title()
            queryset = State.objects.filter(name=state_name)
        else:
            queryset = State.objects.none()
        return queryset

    def to_internal_value(self, data):
        if state_name := data.strip().title():
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
            country_name = country_name.strip().title()
            queryset = Country.objects.filter(name=country_name)
        else:
            queryset = Country.objects.none()
        return queryset

    def to_internal_value(self, data):
        country_name = data.strip().title()
        if country_name:
            country = Country.objects.filter(name=country_name).first()
            if country:
                return country
            raise serializers.ValidationError("Invalid country name")

    def to_representation(self, value):
        return value.name


class DynamicPhoneNumberField(PhoneNumberField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_internal_value(self, data):
        value = super().to_internal_value(data)
        country_name = self.parent.initial_data.get("country")
        try:
            country = Country.objects.get(name=country_name.strip().title())
        except Country.DoesNotExist:
            raise serializers.ValidationError("Invalid country")

        phone_number = PhoneNumber.from_string(value)
        if not phone_number.is_valid() or phone_number.country_code != country.code:
            raise serializers.ValidationError(
                "Invalid phone number for the selected country"
            )

        return value


class AddressSerializer(serializers.ModelSerializer):
    state = StateName(slug_field="name")
    country = CountryName(slug_field="name")
    zip_code = serializers.CharField(max_length=10)
    phone_number = DynamicPhoneNumberField(required=False)

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
        country_name = self.initial_data.get("country")
        try:
            country = Country.objects.get(name=country_name.strip().title())
        except Country.DoesNotExist:
            raise serializers.ValidationError("Invalid country")

        zip_code_regex = country.zipcode_regex
        if zip_code_regex and not re.match(zip_code_regex, value):
            raise serializers.ValidationError("Invalid zip code")

        return value

    def validate_state(self, value):
        country_name = self.initial_data.get("country")
        try:
            country = Country.objects.get(name=country_name.strip().title())
        except Country.DoesNotExist:
            raise serializers.ValidationError("Invalid country")

        if country.state_set.exists() and not value:
            raise serializers.ValidationError(
                "State is required for the selected country."
            )

        return value

    # def validate_phone_number(self, value):
    #     country_name = self.initial_data.get("country")
    #     try:
    #         country = Country.objects.get(name=country_name.strip().title())
    #     except Country.DoesNotExist:
    #         raise serializers.ValidationError("Invalid country")

    #     if country.phone_regex and not re.match(country.phone_regex, value):
    #         raise serializers.ValidationError("Invalid phone number")

    #     return value
