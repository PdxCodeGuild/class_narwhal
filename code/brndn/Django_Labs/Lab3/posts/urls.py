from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('upload/', views.PostCreate.as_view()),
    path('post/<int:pk>/', views.PostView.as_view(), name='post'),
    path('post/create/', views.PostCreate.as_view(), name='create'),
    path('post/<int:pk>/edit/', views.PostEdit.as_view(), name='edit'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)