from django.urls import path, include
from drugs.urls import router as drugrouter

urlpatterns = [
    path('', include(drugrouter.urls)),
]