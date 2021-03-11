from django.db import models
from django.utils import timezone
import datetime

class URLS(models.Model):
    long_url = models.URLField(unique=True)
    short_code = models.URLField(unique=True)

    def __str__(self):
        return self.short_code