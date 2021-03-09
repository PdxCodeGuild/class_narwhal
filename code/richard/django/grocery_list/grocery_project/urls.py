from django.contrib import admin
from django.urls import path

from grocery_list.views import grocery_list

app_name = 'grocery_list'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', grocery_list)
]
