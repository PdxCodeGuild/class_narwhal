from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import GroceryItem

def index(request):
    incomplete_items = GroceryItem.objects.filter(completion_status=False)
    complete_items = GroceryItem.objects.filter(completion_status=True)
    context = {'incomplete_items': incomplete_items, 'complete_items': complete_items}
    return render(request, 'grocery/index.html', context)

def add_item(request):
    GroceryItem.objects.create(item_text=request.POST['item'])
    return HttpResponseRedirect(reverse('grocery:index'))

def complete_item(request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    item.completion_status = True
    item.completed_date = timezone.now()
    item.save()
    return HttpResponseRedirect(reverse('grocery:index'))

def delete_item(request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    item.delete()
    return HttpResponseRedirect(reverse('grocery:index'))

def re_list_item(request, item_id):
    item = get_object_or_404(GroceryItem, pk=item_id)
    item.completion_status = False
    item.save()
    return HttpResponseRedirect(reverse('grocery:index'))