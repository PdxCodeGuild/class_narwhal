from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    tweet_body = models.CharField(max_length=256)
    created_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    #Implement after CreateView and UpdateView
    def get_absolute_url(self):
        return reverse('posts:detail', args=(self.id,))

    class Meta:
        ordering = ['-created_date']
    
