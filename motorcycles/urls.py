# Separate URL configuration for the motorcycles app

from django.urls import path
from .views import MotorcycleCreateView, MotorcycleDeleteView, MotorcycleListView, MotorcycleDetailView, MotorcycleUpdateView

urlpatterns = [
    path('', MotorcycleListView.as_view(), name='motorcycle_list'),
    path('<int:pk>/', MotorcycleDetailView.as_view(), name='motorcycle_detail'),
    path('<int:pk>/update/', MotorcycleUpdateView.as_view(),
         name='motorcycle_update'),
    path('<int:pk>/delete/', MotorcycleDeleteView.as_view(),
         name='motorcycle_delete'),
    path('create/', MotorcycleCreateView.as_view(),
         name='motorcycle_create'),
]
