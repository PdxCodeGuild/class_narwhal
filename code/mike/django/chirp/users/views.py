from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Profile, MyModel

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class UserProfileView(DetailView):
    model = User
    template_name = 'user_profile.html'
    fields = ['location', 'bio']
    context_object_name = 'user_profile'

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class UserEditProfile(UpdateView):
    model = Profile
    template_name = 'user_edit.html'
    fields = ['location', 'bio']

    def get_object(self):
        try:
            return get_object_or_404(User, username=self.kwargs['username']).profile
        except Profile.DoesNotExist:
            return Profile.objects.create(user=get_object_or_404(User, username=self.kwargs['username']))

    def test_func(self):
        user = self.get_object()
        return self.request.user == user.author

def upload_image(request):
    my_image = request.FILES['my_image']
    model = MyModel(..., my_image=my_image)
    model.save()