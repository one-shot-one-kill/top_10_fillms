from django.urls import path

from . import views
from .feeds import LatestFilmFeed

urlpatterns = [
    path('', views.main, name='main'),
    path('feed/', LatestFilmFeed(), name='film_feed'),
    path('films/year/<str:year>/', views.filter_year, name='filter_year'),
    path('films/country/<str:country>/', views.filter_country, name='filter_country'),
    path('films/tag/<str:tag>/', views.filter_tag, name='filter_tag'),
    path('<slug:film>/', views.detail, name='detail'),
]