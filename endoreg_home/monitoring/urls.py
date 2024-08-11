from django.urls import path
from .views import network_devices_view

urlpatterns = [
    path('monitoring/network_devices/', network_devices_view, name='network_devices'),
]
