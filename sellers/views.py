from dj_rest_auth.registration.views import RegisterView
from rest_framework import status
from rest_framework.response import Response
from .serializers import SellerRegistrationSerializer

class SellerRegistrationAPIView(RegisterView):
    serializer_class = SellerRegistrationSerializer