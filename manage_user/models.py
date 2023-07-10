from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class CustomUser(AbstractUser):
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email_active_code = models.CharField(max_length=100, verbose_name='کد فعال سازی ایمیل', editable=False, null=True, blank=True)
    address = models.CharField(max_length=255)
    birth_date = models.DateField(default=timezone.now)
    gender = models.CharField(max_length=10)


    def get_full_name(self):
        return self.username