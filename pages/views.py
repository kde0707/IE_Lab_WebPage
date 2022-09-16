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

def research(request):
    return render(
        request,
        'pages/research.html'
    )

def publications(request):
    return render(
        request,
        'pages/publications.html'
    )

def gallery(request):
    return render(
        request,
        'pages/gallery.html'
    )

def publicationsCon(request):
    return render(
        request,
        'pages/publicationsCon.html'
    )

def publicationsPatents(request):
    return render(
        request,
        'pages/publicationsPatents.html'
    )

    