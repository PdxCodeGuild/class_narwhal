from django.db import models

class Shortcode(models.Model):
    url_long = models.URLField()
    url_short = models.CharField(max_length=6)


    def __str__(self):
        return self.url_short

    
