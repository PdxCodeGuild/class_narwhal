from django.db import models
from django.urls import reverse

class Profile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    location = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('users:profile', args=(self.user.username,))
