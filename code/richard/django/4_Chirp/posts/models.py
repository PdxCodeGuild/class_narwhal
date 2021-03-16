from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Post(models.Model):
    content = models.TextField(max_length=140)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content[:30]

    def get_absolute_url(self):
        return reverse('posts:post_detail', args=[str(self.id)])
    
