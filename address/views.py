from django.shortcuts import render
from .models import Country, State
# Create your views here.
from rest_framework import viewsets
from .serializers import AddressSerializer
from .models import Address

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

