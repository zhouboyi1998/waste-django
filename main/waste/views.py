from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Waste
from .serializers import WasteSerializer


# Create your views here.


class WasteView(ModelViewSet):
    queryset = Waste.objects.all()
    serializer_class = WasteSerializer
