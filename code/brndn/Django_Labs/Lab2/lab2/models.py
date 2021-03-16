import random
import string

from django.db import models

class url_to_code(models.Model):
    url_text = models.TextField()
    code = models.CharField(max_length=6)

    def __str__(self):
        return self.url_text
    
    def random_code(self):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=6))
