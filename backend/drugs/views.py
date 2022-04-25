from django.shortcuts import render
from rest_framework import viewsets

#models and serializers
from django.contrib.auth import get_user_model
from .models import Drug
from .serializers import DrugSerializer

#filters and search
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.prefetch_related('manufacturer_name', 'drug_type', 'pack_size_label', 'short_composition', 'data_source')
    serializer_class = DrugSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['manufacturer_name',]
    search_fields = ['name','manufacturer_name__name','short_composition__short_composition']


