import pytest

from faker import Faker


fake = Faker()


class TestCustomUserModel:
    def test_custom_user_str(self, user):
        assert str(user) == user.username

    def test_custom_user_is_seller(self, user, seller):
        assert isinstance(user.is_seller, bool)
        assert isinstance(seller.is_seller, bool)

    def test_custom_user_get_user_profile(self, user):
        assert user.get_user_profile() is not None
        assert user.get_user_profile().user == user
        assert user.get_seller_profile() is None

    def test_custom_user_get_seller_profile(self, seller):
        assert seller.get_seller_profile() is not None
        assert seller.get_seller_profile().user == seller
        assert seller.get_user_profile() is None

    def test_custom_user_get_profile(self, user, seller):
        if user.is_seller:
            assert user.get_profile() == ("seller", user.get_seller_profile())
        else:
            assert user.get_profile() == ("user", user.get_user_profile())
        if seller.is_seller:
            assert seller.get_profile() == ("seller", seller.get_seller_profile())
        else:
            assert seller.get_profile() == ("user", seller.get_user_profile())

    def test_custom_user_create_profile(self, user, seller):
        assert user.get_user_profile() is not None
        assert seller.get_seller_profile() is not None
