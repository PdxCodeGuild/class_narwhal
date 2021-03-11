from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import GroceryItem


def index(request):
    list_of_items = GroceryItem.objects.filter(completed=False).order_by('created_date')
    completed_items = GroceryItem.objects.filter(completed=True).order_by('completed_date')
    context = {'list_of_items':list_of_items, 'completed_items': completed_items}
    return render(request, 'grocery_list/index.html', context)

def add(request):
    add_item = request.POST['item']
    GroceryItem.objects.create(text_description=add_item)
    return HttpResponseRedirect(reverse('grocery_list:index'))

def completed(request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    item.completed = True
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))

def deleted(request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    item.delete()
    return HttpResponseRedirect(reverse('grocery_list:index'))