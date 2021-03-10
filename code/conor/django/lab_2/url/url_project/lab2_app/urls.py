from django.contrib import admin
from django.urls import path
from . import views


app_name = 'lab2_app'
urlpatterns = [
    path('', views.index, name='index'),
]