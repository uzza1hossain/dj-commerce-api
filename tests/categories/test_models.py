import pytest
from tests.factories import CategoriesFactory

@pytest.mark.django_db
class TestCategoriesModel:

    def setup(self):
        self.category = CategoriesFactory()

    def test_category_str(self):
        assert self.category.__str__() == self.category.name
        assert str(self.category) == self.category.name
        
    def test_category_get_absolute_url(self):
        assert self.category.get_absolute_url() == f"/api/v1/categories/{self.category.slug}/"
