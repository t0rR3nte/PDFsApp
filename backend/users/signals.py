from django.db.models.signals import post_save
from django.dispatch import receiver
from django_otp.plugins.otp_totp.models import TOTPDevice
from .models import CustomUser

@receiver(post_save, sender=CustomUser)
def create_otp_device(sender, instance, created, **kwargs):
    if created and not instance.otp_device:
        otp_device = TOTPDevice.objects.create(user=instance, confirmed=True)
        instance.otp_device = otp_device
        instance.save()
