import random
import re

import pytest
from address.models import Country
from address.models import State
from allauth.account.models import EmailAddress
from django.core import mail
from django.core.management import call_command
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import force_authenticate
from tests.factories import AddressFactory
# from tests.factories import AddressPayloadFactory
from tests.factories import UserFactory
from tests.utils import extract_verification_code_from_email

from users.models import CustomUser

client = APIClient()

fake = Faker()


# @pytest.mark.django_db(transaction=True)
@pytest.mark.usefixtures("load_data")
class TestAddress:
    @pytest.fixture(autouse=True)
    def setup(self, user_factory):
        self.user = user_factory.create()
        self.user.set_password("testpass123")
        self.user.save()

    # def _send_registration_request(self):
    #     mail.outbox = []
    #     response = client.post("/api/v1/auth/signup/user/", self.payload)
    #     assert response.status_code == status.HTTP_201_CREATED
    #     assert response.data["detail"] == "Verification e-mail sent."

    # def _send_verification_request(self):
    #     verification_code = extract_verification_code_from_email(mail.outbox[0].body)
    #     response = client.post(reverse("rest_verify_email"), {"key": verification_code})

    #     assert response.status_code == status.HTTP_200_OK
    #     assert response.data["detail"] == "ok"

    def _send_login_request(self):
        print(self.user.username)
        response = client.post(
            "/api/v1/auth/login/",
            {
                "username": self.user.username,
                "password": "testpass123",
            },
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data["access"] != ""
        return response
    
    def test_example(self):
        response = self._send_login_request()
        access = response.data["access"]
        address = AddressFactory.build().__dict__
        print(address)
        payload = {
            "street_address": address["street_address"],
            "apt": address["apt"],
            "city": address["city"],
            "state": address.get("state", ""),
            "country": address["country"],
            "zip_code": address["zip_code"],
            "phone_number": address["phone_number"],
        }
        print(payload)
        # assert 1 == 2
        # country = Country.objects.order_by("?").first()
        # state = State.objects.filter(country=country).order_by("?").first()

        # zip_code = (
        #     re.sub(r"\#", str(random.randint(0, 9)), country.zipcode_regex)
        #     if country.zipcode_regex
        #     else fake.zipcode()
        # )
        # print(fake.street_address())
        # print(country, state, zip_code)
        # payload = {
        #     "street_address": fake.street_address(),
        #     "apt": fake.building_number(),
        #     "city": fake.city(),
        #     "state": state.name if state else "",
        #     "country": country.name,
        #     "zip_code": zip_code,
        # }
        headers = {
            "HTTP_AUTHORIZATION": f"Bearer {access}",
            "jwtHeaderAuth": f"Bearer {access}",
        }
        response = client.post(
            reverse("address-create"), data={**address}, headers=headers
        )
        print(response.data)
        assert 1 == 2
