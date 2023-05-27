from datetime import timedelta

import pytest
from allauth.account.models import EmailAddress
from allauth.account.models import EmailConfirmation
from allauth.account.models import EmailConfirmationHMAC
from dj_rest_auth.registration.views import VerifyEmailView
from django.core import mail
from django.urls import reverse
from django.utils import timezone
from django.utils.crypto import salted_hmac
from freezegun import freeze_time
from rest_framework import status
from rest_framework.test import APIClient
from tests.utils import extract_verification_code_from_email

from users.models import CustomUser
from users.models import SellerProfile
from users.models import UserProfile

client = APIClient()


@pytest.mark.django_db(transaction=True)
class TestAuthEndpoints:
    @pytest.fixture(autouse=True)
    def setup(self, user_registration_payload_factory):
        self.payload = user_registration_payload_factory()
        self.seller_payload = user_registration_payload_factory()
        self.user = None
        mail.outbox = []

    def _send_registration_request(self):
        mail.outbox = []
        response = client.post("/api/v1/auth/signup/user/", self.payload)
        print(response.data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["detail"] == "Verification e-mail sent."

    def _assert_user_created(self):
        user = CustomUser.objects.get(username=self.payload["username"])
        user_profile = UserProfile.objects.last()

        assert CustomUser.objects.count() == 1
        assert UserProfile.objects.count() == 1
        assert user.username == self.payload["username"]
        assert user.email == self.payload["email"]
        assert user_profile.user == user

    def _send_seller_registration_request(self):
        mail.outbox = []
        response = client.post("/api/v1/auth/signup/seller/", self.seller_payload)
        print(response.data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["detail"] == "Verification e-mail sent."

    def _assert_seller_created(self):
        user = CustomUser.objects.get(username=self.seller_payload["username"])
        seller_profile = SellerProfile.objects.last()

        assert CustomUser.objects.count() == 1
        assert SellerProfile.objects.count() == 1
        assert user.username == self.seller_payload["username"]
        assert user.email == self.seller_payload["email"]
        assert seller_profile.user == user

    def _assert_email_sent(self):
        assert len(mail.outbox) == 1

    def test_create_user(self):
        self._send_registration_request()
        self._assert_user_created()
        self._assert_email_sent()

    def test_create_user_with_invalid_email(self):
        self.payload["email"] = "invalid_email"
        response = client.post("/api/v1/auth/signup/user/", self.payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["email"][0] == "Enter a valid email address."

    def test_create_user_with_invalid_password(self):
        self.payload["password1"] = "123"
        self.payload["password2"] = "123"
        response = client.post("/api/v1/auth/signup/user/", self.payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            "This password is too short. It must contain at least 8 characters."
            in response.data["password1"]
        )

    def test_create_user_with_duplicate_username_and_email(self):
        self._send_registration_request()
        response = client.post("/api/v1/auth/signup/user/", self.payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            response.data["username"][0] == "A user with that username already exists."
        )
        assert (
            response.data["email"][0]
            == "A user is already registered with this e-mail address."
        )

    def test_create_seller(self):
        self._send_seller_registration_request()
        self._assert_seller_created()
        self._assert_email_sent()

    def test_create_seller_with_invalid_email(self):
        self.seller_payload["email"] = "invalid_email"
        response = client.post("/api/v1/auth/signup/seller/", self.seller_payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["email"][0] == "Enter a valid email address."

    def test_create_seller_with_invalid_password(self):
        self.seller_payload["password1"] = "123"
        self.seller_payload["password2"] = "123"
        response = client.post("/api/v1/auth/signup/seller/", self.seller_payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            "This password is too short. It must contain at least 8 characters."
            in response.data["password1"]
        )

    def test_create_seller_with_duplicate_username_and_email(self):
        self._send_seller_registration_request()
        response = client.post("/api/v1/auth/signup/seller/", self.seller_payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            response.data["username"][0] == "A user with that username already exists."
        )
        assert (
            response.data["email"][0]
            == "A user is already registered with this e-mail address."
        )

    def test_verify_email(self):
        self._send_registration_request()
        verification_code = extract_verification_code_from_email(mail.outbox[0].body)
        response = client.post(reverse("rest_verify_email"), {"key": verification_code})

        assert response.status_code == status.HTTP_200_OK
        assert response.data["detail"] == "ok"

    def test_verify_email_with_invalid_code(self):
        self._send_registration_request()
        response = client.post(reverse("rest_verify_email"), {"key": "invalid_code"})

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] == "Not found."

    def test_verify_email_with_used_code(self):
        self._send_registration_request()
        verification_code = extract_verification_code_from_email(mail.outbox[0].body)
        response = client.post(reverse("rest_verify_email"), {"key": verification_code})

        assert response.status_code == status.HTTP_200_OK
        assert response.data["detail"] == "ok"

        response = client.post(reverse("rest_verify_email"), {"key": verification_code})

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] == "Not found."

    @freeze_time("2023-05-26")
    def test_verify_email_with_expired_code(self):
        self._send_registration_request()
        verification_code = extract_verification_code_from_email(mail.outbox[0].body)
        with freeze_time("2023-05-30"):
            response = client.post(
                reverse("rest_verify_email"), {"key": verification_code}
            )

            assert response.status_code == status.HTTP_404_NOT_FOUND
            assert response.data["detail"] == "Not found."

    def test_resend_verification_email(self):
        self._send_registration_request()
        response = client.post(
            reverse("rest_resend_email"), {"email": self.payload["email"]}
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["detail"] == "ok"

    def test_resend_verification_email_with_invalid_email(self):
        self._send_registration_request()
        response = client.post(reverse("rest_resend_email"), {"email": "invalid_email"})

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["email"][0] == "Enter a valid email address."

    def test_login(self):
        self._send_registration_request()
        verification_code = extract_verification_code_from_email(mail.outbox[0].body)
        response = client.post(reverse("rest_verify_email"), {"key": verification_code})

        response = client.post(
            reverse("rest_login"),
            {
                "username": self.payload["username"],
                "email": self.payload["email"],
                "password": self.payload["password1"],
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["access"] != ""

        self._send_seller_registration_request()
        verification_code = extract_verification_code_from_email(mail.outbox[0].body)
        response = client.post(reverse("rest_verify_email"), {"key": verification_code})

        response = client.post(
            reverse("rest_login"),
            {
                "username": self.seller_payload["username"],
                "email": self.seller_payload["email"],
                "password": self.seller_payload["password1"],
            },
        )

        assert response.status_code == status.HTTP_200_OK
        assert response.data["access"] != ""

    def test_login_with_invalid_credentials(self):
        self._send_registration_request()
        verification_code = extract_verification_code_from_email(mail.outbox[0].body)
        response = client.post(reverse("rest_verify_email"), {"key": verification_code})

        response = client.post(
            reverse("rest_login"),
            {
                "username": self.payload["username"],
                "email": self.payload["email"],
                "password": "invalid_password",
            },
        )

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        print(response.data)
        # assert (
        #     response.data["non_field_errors"]
        #     == "Unable to log in with provided credentials."
        # )
