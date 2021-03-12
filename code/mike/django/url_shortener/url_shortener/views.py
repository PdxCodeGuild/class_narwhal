from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import URLS
from string import ascii_letters, digits
import random



def index(request):
    return render(request, 'url_shortener/index.html')

def add(request):
    url = request.POST['url']
    ip = request.META['REMOTE_ADDR']
    if url.startswith('https://'):
        url = url
    else:
        url = 'https://' + url
    new_url = ''.join(random.choice(ascii_letters + digits) for x in range(10))
    URLS.objects.create(long_url=url, short_code=new_url, ip=ip)
    context = {'long_url':url, 'short_code':new_url, 'ip':ip}
    return render(request, 'url_shortener/short_url.html', context)

def shortened(request, short_code):
    url = get_object_or_404(URLS, short_code=short_code)
    return HttpResponseRedirect(url.long_url)