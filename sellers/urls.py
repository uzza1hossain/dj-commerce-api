from django.urls import path

from sellers.views import SellerRegistrationAPIView


urlpatterns = [
    path("signup/", SellerRegistrationAPIView.as_view(), name="seller-signup"),
]
