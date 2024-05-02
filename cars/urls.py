from django.urls import path
from .views import CarCreateView, CarDeleteView, CarListView, CarDetailView, CarUpdateView


urlpatterns = [
    path('cars/', CarListView.as_view(), name='car_list'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car_detail'),
    path('cars/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),
    path('cars/create/', CarCreateView.as_view(), name='car_create'),
]
