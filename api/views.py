from rest_framework import generics
from cars.models import Car
from motorcycles.models import Motorcycle
from .serializers import CarSerializer, MotorcycleSerializer


class CarListCreateAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class MotorcycleListCreateAPIView(generics.ListCreateAPIView):
    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer


class MotorcycleRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Motorcycle.objects.all()
    serializer_class = MotorcycleSerializer
