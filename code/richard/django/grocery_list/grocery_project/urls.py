from django.contrib import admin
from django.urls import path

from grocery_list.views import grocery_list, grocery_item_detail

app_name = 'grocery_list'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', grocery_list),
    path('<id>', grocery_item_detail)
]
