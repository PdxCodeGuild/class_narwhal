from django.urls import path
from . import views


app_name = 'grocery' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('add_item', views.add_item, name='add_item'),
    path('<int:item_id>/complete', views.complete_item, name='complete'),
    path('<int:item_id>/delete', views.delete_item, name='delete'),
    path('<int:item_id>/relist', views.re_list_item, name='relist'),
]