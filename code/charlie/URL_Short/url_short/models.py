from django.db import models

class ShortUrl(models.Model):
    long_url = models.URLField(max_length=100)
    short_code = models.CharField(max_length=20)

    def __str__(self):
        return self.short_code


