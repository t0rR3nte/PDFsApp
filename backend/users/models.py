from django.contrib.auth.models import AbstractUser
from django.db import models
from django_otp.plugins.otp_totp.models import TOTPDevice
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_operator = models.BooleanField(default=True)  # Usuario por defecto es operador
    is_approver = models.BooleanField(default=False)  # Solo algunos usuarios pueden aprobar cambios
    otp_device = models.OneToOneField(
        TOTPDevice, null=True, blank=True, on_delete=models.CASCADE
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email