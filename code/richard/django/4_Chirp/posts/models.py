from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.TextField(max_length=140)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:30]
