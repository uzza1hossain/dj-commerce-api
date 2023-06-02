import random
import re
import string

import factory
import pytest
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
from versatileimagefield.image_warmer import VersatileImageFieldWarmer

from users.models import CustomUser
from users.models import SellerProfile
from users.models import UserProfile

fake = Faker()


class CustomUserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    username = FactoryFaker("user_name")
    email = FactoryFaker("email")
    password = factory.PostGenerationMethodCall("set_password", "testpass123")
    is_seller = False
    is_superuser = False

    @factory.post_generation
    def email_address(self, create, extracted, **kwargs):
        if not create:
            return

        email = self.email
        email_address = EmailAddress.objects.create(
            user=self,
            email=email,
            verified=True,
            primary=True,
        )
        self.email = email_address.email
        self.save()


# class UserProfileFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = UserProfile

#     user = factory.SubFactory(CustomUserFactory)
#     profile_picture = factory.django.ImageField(width=100, height=100)

#     @classmethod
#     def _after_postgeneration(cls, obj, create, results=None):
#         if create:
#             # content_type = ContentType.objects.get_for_model(obj)
#             # address = AddressFactory.create(content_type=content_type, object_id=obj.id)
#             # obj.save()
#             warmer = VersatileImageFieldWarmer(
#                 instance_or_queryset=obj,
#                 rendition_key_set="profile_picture",
#                 image_attr="profile_picture",
#             )
#             warmer.warm()


# class SellerProfileFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = SellerProfile

#     user = factory.SubFactory(CustomUserFactory(is_seller=True))
#     profile_picture = factory.django.ImageField(width=100, height=100)

#     @classmethod
#     def _after_postgeneration(cls, obj, create, results=None):
#         if create:
#             # content_type = ContentType.objects.get_for_model(obj)
#             # address = AddressFactory.create(content_type=content_type, object_id=obj.id)
#             # obj.save()
#             warmer = VersatileImageFieldWarmer(
#                 instance_or_queryset=obj,
#                 rendition_key_set="profile_picture",
#                 image_attr="profile_picture",
#             )
#             warmer.warm()


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
