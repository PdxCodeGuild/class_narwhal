from django.urls import path
from . import views

app_name = 'grocery_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<int:item_id>/completed/', views.completed, name='completed'),
    path('<int:item_id>/deleted/', views.deleted, name='deleted'),
]