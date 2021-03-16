from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Shortcode
from .forms import CreateNewShortURL
import random, string





# comment
def home(request):
    if request.method == 'POST':
        form = CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['url_long']
            random_chars_list = list(string.ascii_letters)
            random_chars=''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
        
            s = Shortcode(url_long=original_website, url_short=random_chars)
            s.save()
            return render(request, 'short_urls/url_created.html', {'chars':random_chars})
    else:
        form=CreateNewShortURL()
        context = {'form': form}
        return render(request, 'short_urls/home.html', context)




def redirect(request, url_short):
    url_info = Shortcode.objects.get(url_short=url_short)
    page = url_info.url_long
    return HttpResponseRedirect(page)




def home2(request):
    return render(request, "short_urls/home.html")



