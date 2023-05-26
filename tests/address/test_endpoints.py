import re

import pytest
from dj_rest_auth.registration.views import VerifyEmailView
from django.core import mail
from django.urls import reverse
from rest_framework.test import APIClient
from tests.utils import extract_verification_code_from_email

from users.models import CustomUser
from users.models import SellerProfile
from users.models import UserProfile

client = APIClient()


@pytest.mark.django_db(transaction=True)
class TestAuthEndpoints:
    def test_create_user(self, user_registration_payload_factory):
        payload = user_registration_payload_factory()
        mail.outbox = []
        response = client.post("/api/v1/auth/signup/user/", payload)
        user = CustomUser.objects.get(username=payload["username"])
        user_profile = UserProfile.objects.last()
        assert response.status_code == 201
        assert response.data["detail"] == "Verification e-mail sent."
        assert len(mail.outbox) == 1
        assert CustomUser.objects.count() == 1
        assert UserProfile.objects.count() == 1
        assert user.username == payload["username"]
        assert user.email == payload["email"]
        assert user_profile.user == user

    def test_verify_email(self, user_registration_payload_factory):
        mail.outbox = []
        payload = user_registration_payload_factory()
        register = client.post("/api/v1/auth/signup/user/", payload)
        assert register.status_code == 201
        assert len(mail.outbox) == 1
        verification_code = extract_verification_code_from_email(mail.outbox[0].body)
        
        response = client.post(reverse("rest_verify_email"), {"key": verification_code})

        assert response.status_code == 200
        assert response.data["detail"] == "ok"
