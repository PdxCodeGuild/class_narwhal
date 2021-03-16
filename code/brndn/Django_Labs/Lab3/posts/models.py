from django.db import models
from django.urls import reverse


class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=111)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("posts:detail", args=(self.id,))
    
