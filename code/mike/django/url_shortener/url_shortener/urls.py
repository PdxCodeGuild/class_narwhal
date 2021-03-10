
from django.urls import path
from . import views

app_name = 'url_shortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('submit/', views.submit, name='submit'),
    path('<int:item_id>/redirect/', views.redirect, name='redirect'),
]