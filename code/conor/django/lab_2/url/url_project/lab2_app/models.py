from django.db import models

# Create your models here.

class shorten(models.Model):
    random_text = models.CharField(max_length=6)
    url_text = models.TextField(max_length=200)

    def __str__(self):
        return self.url_text