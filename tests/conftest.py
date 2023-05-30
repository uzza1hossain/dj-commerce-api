import pytest
from address.models import Country
from django.core.management import call_command
from pytest_factoryboy import register
from tests.factories import AddressFactory
from tests.factories import UserFactory
from tests.factories import UserRegistrationPayloadFactory


@pytest.fixture(autouse=True)
@pytest.mark.django_db
def load_data(db):
    # Country.objects.all().delete()

    call_command(
        "loaddata",
        "/Users/uzzal/Development/Python/Django/dj-commerce-api/address/management/commands/json_data/data.json",
    )


register(AddressFactory)
register(UserRegistrationPayloadFactory)
register(UserFactory)


@pytest.fixture
def user_registration_payload_fixture():
    return UserRegistrationPayloadFactory()
