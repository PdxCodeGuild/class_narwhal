import datetime

from django.db import models
from django.utils import timezone


class GroceryItem(models.Model):
    item_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    completed_date = models.DateTimeField(blank=True, null=True)
    completion_status = models.BooleanField(default=False)

    def __str__(self):
        return self.item_text

    
