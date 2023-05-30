import random
import re
import string

import factory
from address.models import Address
from address.models import Country
from address.models import State
from allauth.account.models import EmailAddress
from faker import Faker
from faker.providers import BaseProvider
from faker_e164.providers import E164Provider
from pytest_factoryboy import named_model

from users.models import CustomUser

fake = Faker()
fake.add_provider(E164Provider)


class ZipCodeProvider(BaseProvider):
    def zip_code_with_pattern(self, pattern):
        return re.sub(r"\#", lambda x: str(random.randint(0, 9)), pattern)


fake.add_provider(ZipCodeProvider)


class UserRegistrationPayloadFactory(factory.Factory):
    class Meta:
        model = named_model(dict, "UserRegistrationPayload")

    # username = factory.Sequence(lambda n: f"user{n:03}")
    username = factory.Sequence(lambda n: f"user{n:03}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password1 = "testpass123"
    password2 = "testpass123"
    print("UserRegistrationPayloadFactory called")


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


# class AddressPayloadFactory(factory.Factory):
#     class Meta:
#         model = named_model(dict, "AddressPayload")

#     street_address = factory.Sequence(lambda n: f"Street {n}")
#     apt = factory.Sequence(lambda n: f"Apt {n}")
#     city = fake.city()

#     @factory.lazy_attribute
#     def country(self):
#         country = Country.objects.order_by("?").first()
#         return country.name
#         # return {
#         #     "id": country.id,
#         #     "name": country.name,
#         #     # Add other fields as needed
#         # }

#     @factory.lazy_attribute
#     def state(self):
#         state = (
#             State.objects.filter(country=Country.objects.get(name=self.country))
#             .order_by("?")
#             .first()
#         )
#         return state.name if state else ""
#         # return {
#         #     "id": state.id,
#         #     "name": state.name,
#         #     # Add other fields as needed
#         # }

#     @factory.lazy_attribute
#     def zip_code(self):
#         country = Country.objects.get(name=self.country)
#         zipcode_regex = country.zipcode_regex
#         if zipcode_regex:
#             pattern = re.sub(r"\#", r"\\d", zipcode_regex)
#             zip_code = fake.zipcode(
#                 pattern=pattern
#             )
#             return zip_code
#         else:
#             return fake.zipcode()


# class AddressFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Address
#         database = "default"

#     # id = factory.Faker("random_int", min=1, max=9999999999)
#     street_address = fake.street_address()
#     apt = fake.secondary_address()
#     city = fake.city()
#     # country = factory.Iterator(Country.objects.all())
#     # country = factory.LazyFunction(lambda: Country.objects.order_by("?").first())
#     phone_number = fake.phone_number()

#     @factory.lazy_attribute
#     def country(self):
#         return Country.objects.order_by("?").first()

#     @factory.lazy_attribute
#     def state(self):
#         country = self.country
#         state = State.objects.filter(country=country).order_by("?").first()
#         return state

#     # @factory.lazy_attribute
#     # def zip_code(self):
#     #     return fake.zipcode(loace)
#     @factory.lazy_attribute
#     def zip_code(self):
#         country = self.country
#         zipcode_regex = country.zipcode_regex
#         if zipcode_regex:
#             zip_code = fake.zip_code_with_pattern(zipcode_regex)
#             if len(zip_code) > 10:
#                 zip_code = zip_code[:10]
#             return zip_code
#         else:
#             return fake.zipcode()

#     # @factory.lazy_attribute
#     # def zip_code(self):
#     #     zipcode_regex = self.country.zipcode_regex

#     #     if zipcode_regex:
#     #         zip_code = re.sub(r"\#", str(random.randint(0, 9)), zipcode_regex)
#     #         return fake.regexify(zip_code)
#     #     else:
#     #         return fake.zipcode()

#     # @factory.lazy_attribute
#     # def phone_number(self):
#     #     phone_number = fake.phone_number()
#     #     extension = random.randint(100, 999)
#     #     return f"{phone_number} ext. {extension}"


def generate_zip_code(zip_code_regex):
    pattern = zip_code_regex.replace("#", string.digits).replace(
        "A", string.ascii_uppercase
    )
    return "".join(random.choice(pattern) for _ in range(len(zip_code_regex)))


class AddressFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Address

    street_address = factory.Faker("street_address")
    apt = factory.Faker("building_number")
    city = factory.Faker("city")
    country = factory.lazy_attribute(lambda _: Country.objects.order_by("?").first())
    state = factory.lazy_attribute(
        lambda obj: State.objects.filter(country=obj.country).first()
    )
    zip_code = factory.lazy_attribute(
        lambda obj: generate_zip_code(obj.country.zipcode_regex)
    )

    phone_number = factory.LazyAttribute(
        lambda obj: fake.e164(region_code="AU", valid=True, possible=True)
    )
