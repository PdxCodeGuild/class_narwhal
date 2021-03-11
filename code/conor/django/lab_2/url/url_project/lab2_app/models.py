from django.db import models

# Create your models here.

class shorten(models.Model):
    random_text = models.CharField(max_length=6)
    url_text = models.TextField(max_length=200)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f'code: {self.random_text}, url: {self.url_text}'