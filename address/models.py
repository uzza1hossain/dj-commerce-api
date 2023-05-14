from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from phonenumber_field.modelfields import PhoneNumberField


class Country(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=5)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Address(models.Model):
    street_address = models.CharField(max_length=255)
    apt = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = ChainedForeignKey(State, chained_field="country", chained_model_field="country", show_all=False, auto_choose=True)  # type: ignore
    zip_code = models.CharField(max_length=10)
    phone_number = PhoneNumberField(blank=True)
