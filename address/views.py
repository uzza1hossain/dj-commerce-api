# Create your views here.
from rest_framework import generics

from .models import Address
from .permissions import IsUserOrSeller
from .serializers import AddressSerializer


class AddressCreateAPIView(generics.CreateAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()
    permission_classes = [IsUserOrSeller]

    def perform_create(self, serializer):
        user = self.request.user
        if hasattr(user, "user_profile"):
            serializer.save(associated_profile=user.user_profile)  # type: ignore
        elif hasattr(user, "seller_profile"):
            serializer.save(associated_profile=user.seller_profile)  # type: ignore
