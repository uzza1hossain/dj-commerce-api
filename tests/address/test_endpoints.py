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
from users.models import UserProfile

client = APIClient()


@pytest.mark.django_db(transaction=True)
class TestAuthEndpoints:
    def test_create_user(self, user_registration_payload_factory):
        payload = user_registration_payload_factory()
        mail.outbox = []
        response = client.post("/api/v1/auth/signup/user/", payload)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["detail"] == "Verification e-mail sent."
        assert len(mail.outbox) == 1

        user = CustomUser.objects.get(username=payload["username"])
        user_profile = UserProfile.objects.last()

        assert CustomUser.objects.count() == 1
        assert UserProfile.objects.count() == 1
        assert user.username == payload["username"]
        assert user.email == payload["email"]
        assert user_profile.user == user

    def test_create_user_with_invalid_email(self, user_registration_payload_factory):
        payload = user_registration_payload_factory(email="invalid_email")
        response = client.post("/api/v1/auth/signup/user/", payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["email"][0] == "Enter a valid email address."

    def test_create_user_with_invalid_password(self, user_registration_payload_factory):
        payload = user_registration_payload_factory(password1="123", password2="123")
        response = client.post("/api/v1/auth/signup/user/", payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        # assert response.data["password"][0] == "This password is too short. It must contain at least 8 characters."

    def test_create_user_with_invalid_username(self, user_registration_payload_factory):
        payload = user_registration_payload_factory()
        first_user = client.post("/api/v1/auth/signup/user/", payload)
        response = client.post("/api/v1/auth/signup/user/", payload)

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert (
            response.data["username"][0] == "A user with that username already exists."
        )

    def test_verify_email(self, user_registration_payload_factory):
        mail.outbox = []
        payload = user_registration_payload_factory()
        register = client.post("/api/v1/auth/signup/user/", payload)

        assert register.status_code == status.HTTP_201_CREATED
        assert len(mail.outbox) == 1

        verification_code = extract_verification_code_from_email(mail.outbox[0].body)
        response = client.post(reverse("rest_verify_email"), {"key": verification_code})

        assert response.status_code == status.HTTP_200_OK
        assert response.data["detail"] == "ok"

    def test_verify_email_with_invalid_code(self, user_registration_payload_factory):
        mail.outbox = []
        payload = user_registration_payload_factory()
        register = client.post("/api/v1/auth/signup/user/", payload)

        assert register.status_code == status.HTTP_201_CREATED
        assert len(mail.outbox) == 1

        response = client.post(reverse("rest_verify_email"), {"key": "invalid_code"})

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] == "Not found."

    def test_verify_email_with_user_code(self, user_registration_payload_factory):
        mail.outbox = []
        payload = user_registration_payload_factory()
        register = client.post("/api/v1/auth/signup/user/", payload)

        assert register.status_code == status.HTTP_201_CREATED
        assert len(mail.outbox) == 1

        verification_code = extract_verification_code_from_email(mail.outbox[0].body)
        response = client.post(reverse("rest_verify_email"), {"key": verification_code})

        assert response.status_code == status.HTTP_200_OK
        assert response.data["detail"] == "ok"

        response = client.post(reverse("rest_verify_email"), {"key": verification_code})

        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.data["detail"] == "Not found."

    @freeze_time("2023-05-26")
    def test_verify_email_with_expired_code(self, user_registration_payload_factory):
        mail.outbox = []
        payload = user_registration_payload_factory()
        register = client.post("/api/v1/auth/signup/user/", payload)

        assert register.status_code == status.HTTP_201_CREATED
        assert len(mail.outbox) == 1

        verification_code = extract_verification_code_from_email(mail.outbox[0].body)
        with freeze_time("2023-05-30"):
            response = client.post(
                reverse("rest_verify_email"), {"key": verification_code}
            )

            assert response.status_code == status.HTTP_404_NOT_FOUND
            assert response.data["detail"] == "Not found."
        response = client.post(reverse("rest_verify_email"), {"key": verification_code})
        
    
        
