import random, string

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse

from .models import url_to_code

def index(request):
    return render(request, 'lab2/index.html')

def random_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def add_url(request):
    url = url_to_code.objects.create(url_text=request.POST['url'], code=random_code())
    return render(request, 'lab2/redirect.html', {'url':url})

def redirect(request, code):
    url = get_object_or_404(url_to_code, code=code)
    print(url.code)
    return HttpResponseRedirect(url.url_text)