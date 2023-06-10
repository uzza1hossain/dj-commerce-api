import pytest
from rest_framework.test import APIClient
from tests.factories import CategoriesFactory
from tests.factories import CustomUserFactory


@pytest.mark.django_db
class TestCAtegoryViewSet:
    def setup(self):
        self.category = CategoriesFactory()
        self.client = APIClient()
        self.super_user = CustomUserFactory(is_superuser=True)
        self.seller = CustomUserFactory(is_seller=True)
        self.user = CustomUserFactory()

        CategoriesFactory.create_batch(10)

    def test_category_create(self):
        self.client.force_authenticate(user=self.seller)
        response = self.client.post("/api/v1/categories/", {"name": "test category"})
        assert response.status_code == 201
        assert response.json()["name"] == "test category"
        self.client.logout()

    def test_category_create_unauthenticated(self):
        response = self.client.post("/api/v1/categories/", {"name": "test category"})
        assert response.status_code == 401
        assert (
            response.json()["detail"] == "Authentication credentials were not provided."
        )

    def test_category_create_unauthorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/v1/categories/", {"name": "test category"})
        print(response.json())
        assert response.status_code == 403
        assert (
            response.json()["detail"]
            == "You do not have permission to perform this action."
        )
        self.client.logout()

    def test_category_partial_update(self):
        self.client.force_authenticate(user=self.seller)
        response = self.client.patch(
            f"/api/v1/categories/{self.category.slug}/",
            {"name": "updated category"},
        )
        assert response.status_code == 200
        assert response.json()["name"] == "updated category"
        self.client.logout()

    def test_category_partial_update_unauthenticated(self):
        response = self.client.patch(
            f"/api/v1/categories/{self.category.slug}/", {"name": "updated category"}
        )
        assert response.status_code == 401
        assert (
            response.json()["detail"] == "Authentication credentials were not provided."
        )

    def test_category_partial_update_unauthorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(
            f"/api/v1/categories/{self.category.slug}/", {"name": "updated category"}
        )
        assert response.status_code == 403
        assert (
            response.json()["detail"]
            == "You do not have permission to perform this action."
        )
        self.client.logout()

    def test_category_update(self):
        self.client.force_authenticate(user=self.seller)
        response = self.client.put(
            f"/api/v1/categories/{self.category.slug}/",
            {"name": "updated category"},
        )
        assert response.status_code == 200
        assert response.json()["name"] == "updated category"
        self.client.logout()

    def test_category_update_unauthenticated(self):
        response = self.client.put(
            f"/api/v1/categories/{self.category.slug}/", {"name": "updated category"}
        )
        assert response.status_code == 401
        assert (
            response.json()["detail"] == "Authentication credentials were not provided."
        )

    def test_category_update_unauthorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            f"/api/v1/categories/{self.category.slug}/", {"name": "updated category"}
        )
        assert response.status_code == 403
        assert (
            response.json()["detail"]
            == "You do not have permission to perform this action."
        )
        self.client.logout()

    def test_category_delete(self):
        self.client.force_authenticate(user=self.super_user)
        response = self.client.delete(f"/api/v1/categories/{self.category.slug}/")
        assert response.status_code == 204
        self.client.logout()

    def test_category_delete_unauthenticated(self):
        response = self.client.delete(f"/api/v1/categories/{self.category.slug}/")
        assert response.status_code == 401
        assert (
            response.json()["detail"] == "Authentication credentials were not provided."
        )

    def test_category_delete_unauthorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/api/v1/categories/{self.category.slug}/")
        assert response.status_code == 403
        assert (
            response.json()["detail"]
            == "You do not have permission to perform this action."
        )
        self.client.logout()
        self.client.force_authenticate(user=self.seller)
        response = self.client.delete(f"/api/v1/categories/{self.category.slug}/")
        assert response.status_code == 403
        assert (
            response.json()["detail"]
            == "You do not have permission to perform this action."
        )

    def test_category_list(self):
        response = self.client.get("/api/v1/categories/")
        assert response.status_code == 200
        assert response.json()[0]["name"] == self.category.name

    def test_category_detail(self):
        response = self.client.get(f"/api/v1/categories/{self.category.slug}/")
        assert response.status_code == 200
        assert response.json()["name"] == self.category.name

    def test_toggle_active(self):
        self.client.force_authenticate(user=self.super_user)
        response = self.client.patch(
            f"/api/v1/categories/{self.category.slug}/toggle-active/"
        )
        assert response.status_code == 200
        assert (
            response.json()["detail"]
            == f"Toggle successful. Set {self.category.is_active} to {not self.category.is_active}."
        )
        self.client.logout()

    def test_toggle_active_unauthenticated(self):
        response = self.client.patch(
            f"/api/v1/categories/{self.category.slug}/toggle-active/"
        )
        assert response.status_code == 401
        assert (
            response.json()["detail"] == "Authentication credentials were not provided."
        )

    def test_toggle_active_unauthorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(
            f"/api/v1/categories/{self.category.slug}/toggle-active/"
        )
        assert response.status_code == 403
        assert (
            response.json()["detail"]
            == "You do not have permission to perform this action."
        )
        self.client.logout()
        self.client.force_authenticate(user=self.seller)
        response = self.client.patch(
            f"/api/v1/categories/{self.category.slug}/toggle-active/"
        )
        assert response.status_code == 403
        assert (
            response.json()["detail"]
            == "You do not have permission to perform this action."
        )
        self.client.logout()
