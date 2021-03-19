from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'home.html'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['image', 'title', 'body']

    """ def upload_image(request):
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                img_obj = form.instance
                return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
        else:
            form = ImageForm()
        return render(request, 'index.html', {'form': form}) """

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostView(DetailView):
    model = Post
    template_name = 'post.html'
    
class PostEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['image','title', 'body']

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('posts:home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author