from django.db import models
from django.utils import timezone
import datetime

class URLS(models.Model):
    long_url = models.CharField(max_length=200)
    short_code = models.CharField(null= True, max_length=16)
    ip = models.GenericIPAddressField(default='0.0.0.0')

    def __str__(self):
        return f'URL: {self.long_url}, Short URL: {self.short_code}, IP: {self.ip}'