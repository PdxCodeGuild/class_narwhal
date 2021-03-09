from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import GroceryItem
def index(request):
    latest_item_list = GroceryItem.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    context = {'latest_item_list': latest_item_list}
    return render(request, 'grocery/index.html', context)