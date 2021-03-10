from django.urls import path

from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name="index"),
    path('add_item/',views.add_item , name="add_item"),
    path('<int:pk>/delete_item/', views.delete_item, name='delete_item'),
    path('<int:pk>/item_status/', views.item_status, name='item_status')
]