import pytest
from django.core.management import call_command
from pytest_factoryboy import register

from .factories import CustomUserFactory
from .factories import SellerProfileFactory
from .factories import UserFactory
from .factories import UserProfileFactory
from .factories import UserRegistrationPayloadFactory


@pytest.fixture(autouse=True)
@pytest.mark.django_db
def load_data():
    call_command(
        "loaddata",
        "/Users/uzzal/Development/Python/Django/dj-commerce-api/address/management/commands/json_data/data.json",
    )


@pytest.fixture(autouse=True)
@pytest.mark.django_db
def seller_profile():
    return SellerProfileFactory()


@pytest.fixture(autouse=True)
@pytest.mark.django_db
def user_profile():
    return UserProfileFactory()


@pytest.fixture(autouse=True)
@pytest.mark.django_db
def user():
    return CustomUserFactory()


@pytest.fixture(autouse=True)
@pytest.mark.django_db
def seller():
    return CustomUserFactory(is_seller=True)


@pytest.fixture(autouse=True)
@pytest.mark.django_db
def superuser():
    return CustomUserFactory(is_superuser=True)


register(CustomUserFactory)
register(UserRegistrationPayloadFactory)
register(UserFactory)
register(SellerProfileFactory)
register(UserProfileFactory)
