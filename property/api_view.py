from typing import List

from rest_framework.utils import serializer_helpers
from .models import Property
from .serializers import PropertySerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView




class PropertyAPIList(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class  = PropertySerializer
    