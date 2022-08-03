from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Classification
from .serializers import ClassificationSerializer


# Create your views here.

class ClassificationView(ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
