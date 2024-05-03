from rest_framework import generics, permissions
from cars.models import Car
from motorcycles.models import Motorcycle
from .serializers import CarSerializer, MotorcycleSerializer


class CarListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class MotorcycleListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer


class MotorcycleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer