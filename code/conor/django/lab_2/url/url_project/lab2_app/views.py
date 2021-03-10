from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from string import ascii_letters, digits
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