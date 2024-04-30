# Separate URL configuration for the cars app

from django.urls import path
from .views import CarCreateView, CarDeleteView, CarListView, CarDetailView, CarUpdateView

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
    path('create/', CarCreateView.as_view(), name='car_create'),
]
