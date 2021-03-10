from django.urls import path
from . import views

app_name = 'home' # for namespacing

urlpatterns = [
    path('', views.home, name='home')
]