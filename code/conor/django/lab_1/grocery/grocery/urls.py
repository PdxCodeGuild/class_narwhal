from django.urls import path

from . import views

app_name='grocery'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<int:pk>/complete/', views.complete, name='complete'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]