from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from django.shortcuts import render, redirect

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/blog_list.html'
    paginate_by = 3

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'

class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload']

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')