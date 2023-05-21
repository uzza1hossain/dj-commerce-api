import pytest
from address.models import Country
from django.core.exceptions import ValidationError

from .factories import CountryFactory


@pytest.mark.django_db
class TestCountryModel:
    def test_create_country(self):
        # Test creating a country with valid data
        country = Country.objects.create(name="United States", code="US")
        assert country.name == "United States"
        assert country.code == "US"

    def test_create_country_without_name(self):
        # Test creating a country without a name (which should raise a ValidationError)
        with pytest.raises(ValidationError):
            Country.objects.create(code="US")

    def test_create_country_with_duplicate_code(self):
        # Test creating a country with a duplicate code (which should raise a ValidationError)
        Country.objects.create(name="United States", code="US")
        with pytest.raises(ValidationError):
            Country.objects.create(name="Germany", code="US")
