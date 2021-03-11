from django.urls import path
from . import views

app_name = 'url_shortener' # for namespacing

urlpatterns = [
    path('', views.home, name='home'),
    path('url_created', views.url_created, name='created'),
    path('<url_short>', views.redirect, name='redirect'),
]