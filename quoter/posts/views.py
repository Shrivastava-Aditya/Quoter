from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse
from django.views.generic.edit import CreateView
from .models import Posts
# Create your views here.
class PostListView(ListView):
    model = Posts
    template_name = 'home.html'

class PostCreateView(CreateView):
    model = Posts
    template_name = 'post_new.html'
    fields = ['user','body']

    def get_success_url(self):
        return reverse('home')
