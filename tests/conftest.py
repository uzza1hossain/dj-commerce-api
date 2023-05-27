import pytest
from pytest_factoryboy import register
from tests.factories import UserFactory
from tests.factories import UserRegistrationPayloadFactory
register(UserRegistrationPayloadFactory)
register(UserFactory)
@pytest.fixture
def user_registration_payload_fixture():
    return UserRegistrationPayloadFactory()
