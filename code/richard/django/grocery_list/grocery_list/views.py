from django.http import HttpResponse
from django.shortcuts import render
from .models import Grocery_Item

def grocery_list(request):
    grocery_items = Grocery_Item.objects.all()
    print(grocery_items)
    context = {
        "grocery_list": grocery_items
    }
    return render(request, "grocery_list/grocery_list.html", context)



