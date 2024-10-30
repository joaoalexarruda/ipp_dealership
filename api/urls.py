from django.urls import path
from . import views

urlpatterns = [
    path("cars/", views.CarListCreateAPIView.as_view(), name="car_list_create"),
    path(
        "cars/<int:pk>/",
        views.CarRetrieveUpdateDestroyAPIView.as_view(),
        name="car_retrieve_update_destroy",
    ),
    path(
        "motorcycles/",
        views.MotorcycleListCreateAPIView.as_view(),
        name="motorcycle_list_create",
    ),
    path(
        "motorcycles/<int:pk>/",
        views.MotorcycleRetrieveUpdateDestroyAPIView.as_view(),
        name="motorcycle_retrieve_update_destroy",
    ),
]
