from django.urls import path
from .views import current_datetime, async_current_datetime, ppe_current_datetime
urlpatterns = [
    path("", current_datetime, name="current-datetime"),
    path("async", async_current_datetime, name="async-current-datetime"),
    path("async-ppe", ppe_current_datetime, name="ppe-current-datetime"),
]