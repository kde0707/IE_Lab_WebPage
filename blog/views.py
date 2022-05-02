from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/index.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/single_post_page.html'