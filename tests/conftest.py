import pytest
from pytest_factoryboy import register
from tests.factories import UserRegistrationPayloadFactory
register(UserRegistrationPayloadFactory)

@pytest.fixture
def user_registration_payload_fixture():
    return UserRegistrationPayloadFactory()
