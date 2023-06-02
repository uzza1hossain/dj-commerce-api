import random
import re
import string

import factory
from address.models import Address
from address.models import Country
from address.models import State
from allauth.account.models import EmailAddress
from factory import Faker as FactoryFaker
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyChoice
from faker import Faker
from faker.providers import BaseProvider
from faker_e164.providers import E164Provider
from pytest_factoryboy import named_model

from users.models import CustomUser

fake = Faker()


class CustomUserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = FactoryFaker("user_name")
    email = FactoryFaker("email")
    password = FactoryFaker("password")
    is_seller = False

    @factory.post_generation
    def email_address(self, create, extracted, **kwargs):
        if not create:
            return

        email = self.email

        # Create an EmailAddress object for the user
        email_address = EmailAddress.objects.create(
            user=self,
            email=email,
            verified=True,  # Set email address as verified
            primary=True,  # Set email address as primary
        )

        # Update the user's email field with the verified email
        self.email = email_address.email
        self.save()


class UserRegistrationPayloadFactory(factory.Factory):
    class Meta:
        model = named_model(dict, "UserRegistrationPayload")

    # username = factory.Sequence(lambda n: f"user{n:03}")
    username = factory.Sequence(lambda n: f"user{n:03}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password1 = "testpass123"
    password2 = "testpass123"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = factory.Sequence(lambda n: f"user{n:02}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password = "testpass123"

    @factory.post_generation
    def email_address(self, create, extracted, **kwargs):
        if not create:
            return

        email = self.email

        # Create an EmailAddress object for the user
        email_address = EmailAddress.objects.create(
            user=self,
            email=email,
            verified=True,  # Set email address as verified
            primary=True,  # Set email address as primary
        )

        # Update the user's email field with the verified email
        self.email = email_address.email
        self.save()
