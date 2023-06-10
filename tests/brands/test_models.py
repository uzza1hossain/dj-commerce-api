import pytest
from tests.factories import BrandFactory

@pytest.mark.django_db
class TestBrandModel:
    def setup(self):
        self.brand = BrandFactory()

    def test_brand_str(self):
        assert self.brand.__str__() == self.brand.name
        assert str(self.brand) == self.brand.name
