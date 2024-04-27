# Separate URL configuration for the pages app

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('location/', views.location, name='location'),
    path('about/', views.about, name='about'),
]
