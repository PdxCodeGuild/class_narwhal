from django.utils import timezone
from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

from .models import GroceryItem

def index(request):
    # return HttpResponse('Hello World!')
    items = GroceryItem.objects.all()
    context = {'items': items}
    return render(request, 'grocery_list_app/index.html', context)

def add_item(request):
    name = request.POST['name']
    date = timezone.now()
    item = GroceryItem.objects.create(name=name, created_date=date)
    return HttpResponseRedirect(reverse('grocerylist:index'))