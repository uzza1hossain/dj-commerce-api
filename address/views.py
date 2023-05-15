from rest_framework import generics
from rest_framework.generics import ListCreateAPIView

from .models import Address
from .permissions import IsUserOrSeller
from .serializers import AddressSerializer

# Create your views here.


class AddressListCreateAPIView(ListCreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [IsUserOrSeller]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if hasattr(user, "user_profile"):
                return self.request.user.user_profile.get_addresses()  # type: ignore
            elif hasattr(user, "seller_profile"):
                return self.request.user.seller_profile.get_addresses()  # type: ignore
        return Address.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, "user_profile"):
            serializer.save(associated_profile=user.user_profile)
        elif hasattr(user, "seller_profile"):
            serializer.save(associated_profile=user.seller_profile)


class AddressRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [IsUserOrSeller]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, "user_profile"):
            return user.user_profile.get_addresses()  # type: ignore
        elif hasattr(user, "seller_profile"):
            return user.seller_profile.get_addresses()  # type: ignore
        return Address.objects.none()
