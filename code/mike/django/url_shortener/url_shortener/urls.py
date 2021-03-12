
from django.urls import path
from . import views

app_name = 'url_shortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<str:short_code>/', views.shortened, name='shortened'),
]