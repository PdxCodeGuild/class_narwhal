from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import GroceryItem

def index(request):
    latest_grocery_list = GroceryItem.objects.filter(bought=False).order_by('-pub_date')
    bought_groceries = GroceryItem.objects.filter(bought=True).order_by('-completed_date')
    context = {
        'latest_grocery_list': latest_grocery_list,
        'bought_groceries': bought_groceries,
    }
    return render(request, 'grocery_list/index.html', context)

def add_item(request):
    GroceryItem.objects.create(pub_date=timezone.now(), food_item=request.POST['add_item'],bought=False)
    # post = request.POST['add_item']
    #print(type(post)) #****** good for checking you requests *******
    return HttpResponseRedirect(reverse('grocery_list:index'))

def delete_item(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def item_status(request, pk):
    item = get_object_or_404(GroceryItem, pk=pk)
    item.bought = False if item.bought else True
    item.completed_date = timezone.now() if item.bought else None
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))
    


    