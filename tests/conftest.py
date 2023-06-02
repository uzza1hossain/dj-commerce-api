import pytest
from address.models import Country
from django.core.management import call_command
from pytest_factoryboy import register
from tests.factories import CustomUserFactory
from tests.factories import UserFactory
from tests.factories import UserRegistrationPayloadFactory

# from tests.factories import AddressFactory


@pytest.fixture(autouse=True)
@pytest.mark.django_db
def load_data(db):
    call_command(
        "loaddata",
        "/Users/uzzal/Development/Python/Django/dj-commerce-api/address/management/commands/json_data/data.json",
    )


@pytest.fixture
def user():
    return CustomUserFactory()

@pytest.fixture
def seller():
    return CustomUserFactory(is_seller=True)


register(CustomUserFactory)


# register(AddressFactory)
register(UserRegistrationPayloadFactory)
register(UserFactory)


@pytest.fixture
def user_registration_payload_fixture():
    return UserRegistrationPayloadFactory()
