# from django.urls import include
# from django.urls import path
# from rest_framework import routers
# from .views import AddressViewSet
# router = routers.DefaultRouter()
# router.register(r"addresses", AddressViewSet)
# urlpatterns = [
#     # Other URL patterns
#     path("", include(router.urls)),
# ]
from django.urls import path

from .views import AddressListCreateAPIView
from .views import AddressRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("", AddressListCreateAPIView.as_view(), name="address-create"),
    path(
        "<int:pk>/",
        AddressRetrieveUpdateDestroyAPIView.as_view(),
        name="address-detail",
    ),
]
