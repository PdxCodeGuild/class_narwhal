from django.db import models

class Shortcode(models.Model):
    url = models.URLField()
    code = models.CharField(max_length=6)


    def __str__(self):
        return self.code

    
