from django.urls import path
from . import views

app_name = 'grocerylist' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('add-item/', views.add_item, name='add_item'),
]