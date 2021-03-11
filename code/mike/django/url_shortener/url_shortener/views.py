from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import URLS
from string import ascii_letters, digits
import random
import pprint


def index(request):
    return render(request, 'url_shortener/index.html')

def add(request):
    url = request.POST['url']
    new_url = ''.join(random.choice(ascii_letters + digits) for x in range(10))
    URLS.objects.create(long_url=url, short_code=new_url)
    context = {'short_code':new_url}
    return render(request, 'url_shortener/short_url.html', context)

def shortened(request, new_url):
    url = get_object_or_404(URLS, short_code=new_url)
    pprint.pprint(request.META)
    url.clicks += 1
    url.save()
    return HttpResponseRedirect(url.long_url)
    