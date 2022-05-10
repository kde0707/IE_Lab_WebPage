from django.shortcuts import render
from blog.models import Post

# Create your views here.

def landing(request):
    recent_posts = Post.objects.order_by('-pk')[:3]
    return render(
        request,
        'pages/landing.html',
        {
            'recent_posts' : recent_posts,
        }
    )

def about_us(request):
    return render(
        request,
        'pages/about_us.html'
    )