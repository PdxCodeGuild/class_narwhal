from django.urls import path

from . import views

app_name = 'lab2'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_url', views.add_url, name='add_url'),
    path('<str:code>', views.redirect, name='redirect'),
]