from django.urls import path
from .views import DrugViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'drugs', DrugViewSet)