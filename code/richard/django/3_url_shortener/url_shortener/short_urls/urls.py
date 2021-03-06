from django.urls import path
from . import views

app_name = 'url_shortener' # for namespacing

urlpatterns = [
    path('', views.home, name='home'),
    path('<url_short>', views.redirect, name='redirect'),
]