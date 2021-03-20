from django.urls import path

from . import views

app_name= 'posts'

urlpatterns = [
    path('', views.TweetListView.as_view(), name='home'),
    path('post/new/', views.TweetCreateView.as_view(), name='new'),
    path('post/<int:pk>/', views.TweetDetailView.as_view(), name='detail'),
    path('post/<int:pk>/edit/', views.TweetEditView.as_view(), name='edit'),
    path('post/<int:pk>/delete/', views.TweetDeleteView.as_view(), name='delete'),
]
