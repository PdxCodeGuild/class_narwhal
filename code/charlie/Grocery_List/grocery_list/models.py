from django.db import models
from django.utils import timezone
import datetime

class GroceryItem(models.Model):
    pub_date = models.DateTimeField()
    completed_date = models.DateTimeField(null=True, blank=True)
    food_item = models.CharField(max_length=50)
    bought = models.BooleanField(default=False)

    def __str__(self):
        return self.food_item
    
