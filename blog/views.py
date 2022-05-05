from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/blog_list.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/blog_detail.html'