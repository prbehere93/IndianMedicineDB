from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

#models and serializers
from django.contrib.auth import get_user_model
from .models import Drug
from .serializers import DrugSerializer

#filters and search
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

#custom stuff
from .permissions import CustomPermission

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.prefetch_related('manufacturer_name', 'drug_type', 'pack_size_label', 'short_composition', 'data_source').order_by('name')
    serializer_class = DrugSerializer
    permission_classes = [CustomPermission,]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['manufacturer_name','short_composition']
    search_fields = ['name','manufacturer_name__name','short_composition__short_composition'] #the __can be used to search foreign key
    
    # removing the 'delete' method from allowed methods
    # http_method_names = ['get', 'post', 'put', 'patch'] 
    
    # overriding methods in the ViewSet to check how it works
    def list(self, request, *args, **kwargs):
        print("Just checking to see if this works")
        response = super().list(request, *args, **kwargs)
        print(request.data)
        return response

