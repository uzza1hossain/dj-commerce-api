import json

from address.models import Country
from address.models import State
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Populates the Country and State models with data from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Path to the JSON file")

    def handle(self, *args, **options):
        file_path = options["file_path"]

        with open(file_path) as file:
            data = json.load(file)

        for item in data:
            country = Country.objects.create(name=item["Country"], code=item["ISO"])
            for subdivision in item["Subdivisions"]:
                State.objects.create(
                    name=subdivision["Name"], code=subdivision["Code"], country=country
                )

        self.stdout.write(self.style.SUCCESS("Data has been successfully populated."))
