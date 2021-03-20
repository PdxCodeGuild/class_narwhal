from django.db import models

# Create your models here.
class GroceryItem(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateField()
    completed_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name