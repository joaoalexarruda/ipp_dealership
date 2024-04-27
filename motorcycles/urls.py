# Separate URL configuration for the motorcycles app

from django.urls import path
from .views import MotorcycleListView
from . import views

urlpatterns = [
    path('', MotorcycleListView.as_view(), name='motorcycle_list'),
]
