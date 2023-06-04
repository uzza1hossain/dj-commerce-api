import pytest
from django.core.management import call_command
from pytest_factoryboy import register

from .factories import CustomUserFactory
from .factories import UserFactory
from .factories import UserProfileFactory
from .factories import UserRegistrationPayloadFactory

# from .factories import SellerProfileFactory


@pytest.fixture(autouse=True)
@pytest.mark.django_db
def load_data():
    call_command(
        "loaddata",
        "/Users/uzzal/Development/Python/Django/dj-commerce-api/address/management/commands/json_data/data.json",
    )


# @pytest.fixture(autouse=True)
# @pytest.mark.django_db
# def seller_profile():
#     return SellerProfileFactory()


# @pytest.fixture(autouse=True)
# @pytest.mark.django_db
# def user_profile():
#     return UserProfileFactory()


@pytest.fixture
def user():
    return CustomUserFactory()


@pytest.fixture
def seller():
    return CustomUserFactory(is_seller=True)


@pytest.fixture
def superuser():
    return CustomUserFactory(is_superuser=True)


@pytest.fixture(scope="function")
@pytest.mark.django_db
def user_profile(user):
    return UserProfileFactory(user=user)


# register(CustomUserFactory)
register(UserRegistrationPayloadFactory)
register(UserFactory)
# register(SellerProfileFactory)
# register(UserProfileFactory)
