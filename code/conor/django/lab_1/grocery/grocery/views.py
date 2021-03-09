from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import GroceryItem

def index(request):
    current_grocery_list = GroceryItem.objects.filter(completed=False).order_by('date_created')
    completed_items = GroceryItem.objects.filter(completed=True).order_by('date_completed')
    context = {'current_grocery_list': current_grocery_list, 'completed_items': completed_items}
    return render(request, 'grocery/index.html', context)

def add(request):
    grocery_item = request.POST['item']
    GroceryItem.objects.create(item_text=grocery_item)
    return HttpResponseRedirect(reverse('grocery:index'))

def complete(request, pk):
    complete_item = get_object_or_404(GroceryItem, pk=pk)
    complete_item.completed = True
    complete_item.save()
    return HttpResponseRedirect(reverse('grocery:index'))

def delete(request, pk):
    delete_item = get_object_or_404(GroceryItem, pk=pk)
    delete_item.delete()
    return HttpResponseRedirect(reverse('grocery:index'))