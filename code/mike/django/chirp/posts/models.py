from django.db import models
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = models.TextField(max_length=280)

    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.id,))

    class Meta:
        ordering = ['-created']
    
