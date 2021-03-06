from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Post

class TweetListView(ListView):
    model = Post
    template_name = "home.html"

class TweetDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class TweetCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'tweet_body']

class TweetEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'tweet_body']

    def test_user_verify(self):
        post = self.get_object()
        return self.request.user == post.author

class TweetDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:home')

    def test_user_verify(self):
        post = self.get_object()
        return self.request.user == post.author