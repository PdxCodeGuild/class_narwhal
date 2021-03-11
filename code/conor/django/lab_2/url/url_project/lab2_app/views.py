from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from string import ascii_letters, digits
from .models import shorten
import pprint
import random

# Create your views here.

def index(request):
    return render(request, 'lab2_app/index.html')

def rando_code():
    string = ''
    let_num = ascii_letters + digits
    for i in range(6):
        string += random.choice(let_num)
    return string

def submit(request):
    url = request.POST['input_url']
    code = rando_code()
    url_add = shorten(url_text=url, random_text=code)
    url_add.save()
    context = {'random_text': code}
    return render(request, 'lab2_app/changed.html', context)

def redirection(request, code):
    site = get_object_or_404(shorten, random_text=code)
    pprint.pprint(request.META)
    site.clicks += 1
    site.save()
    return HttpResponseRedirect(site.url_text)