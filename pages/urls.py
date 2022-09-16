from django.urls import path
from . import views

urlpatterns = [
    path('about_us/', views.about_us),
    path('research/', views.research),
    path('publications/', views.publications),
    path('gallery/', views.gallery),
    path('publicationsCon/', views.publicationsCon),
    path('publicationsPatents/', views.publicationsPatents),
    path('', views.landing),
]