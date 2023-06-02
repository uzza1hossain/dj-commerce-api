import pytest

@pytest.mark.django_db
class TestCustomUserModel:
    def test_custom_user_str(self, user):
        assert user.__str__() == user.username

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

    def test_custom_user_get_profile(self, user, seller, superuser):
        if user.is_seller:
            assert user.get_profile() == ("seller", user.get_seller_profile())
        else:
            assert user.get_profile() == ("user", user.get_user_profile())
        if seller.is_seller:
            assert seller.get_profile() == ("seller", seller.get_seller_profile())
        else:
            assert seller.get_profile() == ("user", seller.get_user_profile())
        assert superuser.get_profile() == (None, None)

    def test_custom_user_create_profile(self, user, seller, superuser):
        assert user.get_user_profile() is not None
        assert user.get_seller_profile() is None
        assert seller.get_seller_profile() is not None
        assert seller.get_user_profile() is None
        assert superuser.get_user_profile() is None
        assert superuser.get_seller_profile() is None


# @pytest.mark.django_db
# class TestUserProfile:
#     def test_user_profile_str(user_profile):
#         assert str(user_profile) == user_profile.user.username
#         assert user_profile.__str__() == user_profile.user.username

#     #! update this test after creating address factory
#     def test_user_profile_get_addresses(user_profile):
#         address = user_profile.get_addresses().first()
#         assert address is None
#         # assert address.content_object == user_profile


# @pytest.mark.django_db()
# class TestSellerProfile:
#     def test_seller_profile_str(seller_profile):
#         assert str(seller_profile) == seller_profile.user.username
#         assert seller_profile.__str__() == seller_profile.user.username

#     #! update this test after creating address factory
#     def test_seller_profile_get_addresses(seller_profile):
#         address = seller_profile.get_addresses().first()
#         assert address is None
#         # assert address.content_object == seller_profile
