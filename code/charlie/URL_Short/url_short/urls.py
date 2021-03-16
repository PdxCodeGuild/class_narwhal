from django.urls import path

from . import views

app_name = 'url_short'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:short_code>', views.redirect, name='redirect'),
]