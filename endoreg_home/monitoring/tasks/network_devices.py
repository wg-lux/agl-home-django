from celery import shared_task
from endoreg_db.models import NetworkDevice

@shared_task(bind=True)
def ping_devices(self):
    """Ping network devices."""
    for device in NetworkDevice.objects.all():
        device.ping()

