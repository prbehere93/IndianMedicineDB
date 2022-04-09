from django.urls import path
from .views import DrugViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'drugs', DrugViewSet)

urlpatterns = router.urls