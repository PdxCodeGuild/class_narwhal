from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('join/', views.Join.as_view(), name='join'),
    path('<str:username>/', views.Profile.as_view(), name='profile'),
]