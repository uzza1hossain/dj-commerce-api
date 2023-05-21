import factory

from address.models import Country


class CountryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Country

    name = factory.Faker("country")
    code = factory.Sequence(lambda n: f"CODE-{n}")
