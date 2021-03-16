from django.contrib import admin

from .models import MyModel, Post

admin.site.register(Post)
admin.site.register(MyModel)