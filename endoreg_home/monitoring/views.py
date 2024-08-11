from django.shortcuts import render
from endoreg_db.models import NetworkDevice

def network_devices_view(request):
    # Fetch all NetworkDevice objects from the database
    devices = NetworkDevice.objects.all()
    return render(request, 'monitoring/network_devices.html', {'devices': devices})
