from django.db import models
from django.utils import timezone

class GroceryItem(models.Model):
    item_text = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.item_text