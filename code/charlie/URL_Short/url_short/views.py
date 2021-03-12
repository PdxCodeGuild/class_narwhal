from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone

import random

from .models import ShortUrl

def index(request):
    context = {} 
    if request.method == "POST":
        convert_url = request.POST['index']
        # random.shuffle(convert_url)
        temp = ''
        for char in range(0, len(convert_url), 12):
                temp += random.choice(convert_url)
        convert_url = temp
        new_url = ShortUrl.objects.create(long_url=request.POST['index'], short_code=convert_url)
        context = {"new_url": new_url}

    return render(request, 'url_short/index.html', context)
    return HttpResponse("Ok, step 1")

    #  if request.method == "GET":
    #     return HttpResponseRedirect(reverse())

def redirect(request, short_code):
    long_url = get_object_or_404(ShortUrl, short_code=short_code )
    return HttpResponseRedirect(long_url.long_url)