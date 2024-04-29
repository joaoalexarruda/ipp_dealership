# Separate URL configuration for the motorcycles app

from django.urls import path
from .views import MotorcycleListView, MotorcycleDetailView

urlpatterns = [
    path('', MotorcycleListView.as_view(), name='motorcycle_list'),
    path('<int:pk>/', MotorcycleDetailView.as_view(), name='motorcycle_detail'),
]
