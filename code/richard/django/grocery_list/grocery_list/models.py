from django.db import models

class Grocery_Item(models.Model):
    description = models.CharField(max_length=200)
    date_created = models.DateField()
    date_completed = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.description