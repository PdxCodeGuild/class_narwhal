from django.contrib import admin
from django.urls import path

from grocery_list.views import (
    grocery_list,
    grocery_item_detail, 
    item_create,
    item_update,
    item_delete,
) 

app_name = 'grocery_list'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', grocery_list),
    path('item_create', item_create),
    path('<id>', grocery_item_detail),
    path('<id>/update/', item_update),
    path('<id>/delete/', item_delete),
]
