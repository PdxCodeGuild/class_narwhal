from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Grocery_Item
from .forms import ItemForm

def grocery_list(request):
    grocery_items = Grocery_Item.objects.all()
    print(grocery_items)
    context = {
        "grocery_list": grocery_items
    }
    return render(request, "grocery_list/grocery_list.html", context)


def grocery_item_detail(request, id):
    grocery_item = Grocery_Item.objects.get(id=id)
    context = {
        "grocery_item": grocery_item
    }
    return render(request, "grocery_list/item_detail.html", context)


def item_create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, "grocery_list/item_create.html", context)


def item_update(request, id):
    grocery_item = Grocery_Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance = grocery_item)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        return redirect('/')
    context = {"form": form}
    return render(request, "grocery_list/item_update.html", context)


def item_delete(request, id):
    grocery_item = Grocery_Item.objects.get(id=id)
    grocery_item.delete()
    return redirect('/')
