from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.last_name} {self.first_name}'