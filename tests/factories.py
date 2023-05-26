import factory
from faker import Faker
from pytest_factoryboy import named_model

fake = Faker()


class UserRegistrationPayloadFactory(factory.Factory):
    class Meta:
        model = named_model(dict, "UserRegistrationPayload")

    username = factory.Sequence(lambda n: f"user{n:02}")
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")
    password1 = "testpass123"
    password2 = "testpass123"

    # Add more fields as needed

    # @classmethod
    # def _create(cls, model_class, *args, **kwargs):
    #     payload = factory.build(dict, *args, **kwargs)
    #     # You can modify the payload if needed before returning it
    #     return payload
