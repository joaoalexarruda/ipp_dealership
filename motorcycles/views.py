from django.shortcuts import render
from django.views.generic import ListView
from .models import Motorcycle

# Create your views here.


class MotorcycleListView(ListView):
    model = Motorcycle
    template_name = 'motorcycles/motorcycle_list.html'
    context_object_name = 'motorcycle_list'
    
    def get_queryset(self):
        queryset = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(model__icontains=search)
        return queryset