import pytest
from rest_framework import status
from rest_framework.test import APIClient
from tests.factories import BrandFactory
from tests.factories import CustomUserFactory


@pytest.mark.django_db
class TestBrandViewSet:
    def setup(self):
        self.brand = BrandFactory()
        self.client = APIClient()
        self.super_user = CustomUserFactory(is_superuser=True)
        self.seller = CustomUserFactory(is_seller=True)
        self.user = CustomUserFactory()
        BrandFactory.create_batch(10)

    # Helper methods
    def assert_authentication_required(self, response):
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert (
            response.json()["detail"] == "Authentication credentials were not provided."
        )

    def assert_permission_denied(self, response):
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert (
            response.json()["detail"]
            == "You do not have permission to perform this action."
        )

    # Tests
    def test_brand_create(self):
        self.client.force_authenticate(user=self.seller)
        response = self.client.post("/api/v1/brands/", {"name": "test brand"})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["name"] == "test brand"
        assert response.json()["slug"] == "test-brand"
        self.client.logout()

    def test_brand_create_unauthenticated(self):
        response = self.client.post("/api/v1/brands/", {"name": "test brand"})
        self.assert_authentication_required(response)

    def test_brand_create_unauthorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post("/api/v1/brands/", {"name": "test brand"})
        self.assert_permission_denied(response)
        self.client.logout()

    def test_brand_partial_update(self):
        self.brand.owner = self.seller.seller_profile
        self.brand.save()
        self.client.force_authenticate(user=self.seller)
        response = self.client.patch(
            f"/api/v1/brands/{self.brand.slug}/", {"name": "updated brand"}
        )
        print(response.json())
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["name"] == "updated brand"
        self.client.logout()

    def test_brand_partial_update_unauthenticated(self):
        response = self.client.patch(
            f"/api/v1/brands/{self.brand.slug}/", {"name": "updated brand"}
        )
        self.assert_authentication_required(response)

    def test_brand_partial_update_unauthorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(
            f"/api/v1/brands/{self.brand.slug}/", {"name": "updated brand"}
        )
        self.assert_permission_denied(response)
        self.client.logout()

    def test_brand_update(self):
        self.brand.owner = self.seller.seller_profile
        self.brand.save()
        self.client.force_authenticate(user=self.seller)
        response = self.client.put(
            f"/api/v1/brands/{self.brand.slug}/", {"name": "updated brand"}
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["name"] == "updated brand"
        self.client.logout()

    def test_brand_update_unauthenticated(self):
        response = self.client.put(
            f"/api/v1/brands/{self.brand.slug}/", {"name": "updated brand"}
        )
        self.assert_authentication_required(response)

    def test_brand_update_unauthorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.put(
            f"/api/v1/brands/{self.brand.slug}/", {"name": "updated brand"}
        )
        self.assert_permission_denied(response)
        self.client.logout()

    def test_brand_delete(self):
        self.brand.owner = self.seller.seller_profile
        self.brand.save()
        self.client.force_authenticate(user=self.seller)
        response = self.client.delete(f"/api/v1/brands/{self.brand.slug}/")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        self.client.logout()

    def test_brand_delete_unauthenticated(self):
        response = self.client.delete(f"/api/v1/brands/{self.brand.slug}/")
        self.assert_authentication_required(response)

    def test_brand_delete_unauthorized(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/api/v1/brands/{self.brand.slug}/")
        self.assert_permission_denied(response)
        self.client.logout()

    def test_brand_public_delete(self):
        self.brand.owner = self.seller.seller_profile
        self.brand.is_public = True
        self.brand.save()
        self.client.force_authenticate(user=self.seller)
        response = self.client.delete(f"/api/v1/brands/{self.brand.slug}/")
        assert response.status_code == status.HTTP_403_FORBIDDEN
        self.client.logout()

    def test_brand_list(self):
        response = self.client.get("/api/v1/brands/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()[0]["name"] == self.brand.name

    def test_brand_detail(self):
        response = self.client.get(f"/api/v1/brands/{self.brand.slug}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["name"] == self.brand.name
