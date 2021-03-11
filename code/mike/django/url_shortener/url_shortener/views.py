from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import URLS


def index(request):
    list_of_urls = URLS.objects.filter(completed=False).order_by('created_date')
    items_completed = URLS.objects.filter(completed=True).order_by('completed_date')
    context = {'list_of_urls':list_of_urls, 'items_completed':items_completed}
    return render(request, 'grocery_list/index.html', context)

def submit(request):
    add_item = request.POST['item']
    URLS.objects.create(text_description=add_item)
    return HttpResponseRedirect(reverse('grocery_list:redirect'))

def redirect(item_id):
    item = get_object_or_404(URLS, pk=item_id)
    item.completed = True
    item.save()
    return HttpResponseRedirect(reverse('grocery_list:index'))