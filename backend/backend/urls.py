from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/v1/', include('api.urls')),
    path('api/v1/drugs/', include('drugs.urls')),
    path('example/', include('example_app.urls')),
    
]
