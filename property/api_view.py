from typing import List
from rest_framework.decorators import permission_classes

from rest_framework.utils import serializer_helpers
from .models import Property
from .serializers import PropertySerializer
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated



class PropertyAPIList(ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes  = [IsAuthenticated]


class PropertyAPIDetail(RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class  = PropertySerializer
    permission_classes  = [IsAuthenticated]
    