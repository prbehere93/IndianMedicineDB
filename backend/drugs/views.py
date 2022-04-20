from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Drug
from .serializers import DrugSerializer

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.prefetch_related('manufacturer_name', 'drug_type', 'pack_size_label', 'short_composition', 'data_source')
    serializer_class = DrugSerializer

