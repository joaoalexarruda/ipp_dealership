from django.urls import path
from .views import (
    MotorcycleCreateView,
    MotorcycleDeleteView,
    MotorcycleListView,
    MotorcycleDetailView,
    MotorcycleUpdateView,
)


urlpatterns = [
    path("motorcycles/", MotorcycleListView.as_view(), name="motorcycle_list"),
    path(
        "motorcycles/<int:pk>/",
        MotorcycleDetailView.as_view(),
        name="motorcycle_detail",
    ),
    path(
        "motorcycles/<int:pk>/update/",
        MotorcycleUpdateView.as_view(),
        name="motorcycle_update",
    ),
    path(
        "motorcycles/<int:pk>/delete/",
        MotorcycleDeleteView.as_view(),
        name="motorcycle_delete",
    ),
    path(
        "motorcycles/create/", MotorcycleCreateView.as_view(), name="motorcycle_create"
    ),
]
