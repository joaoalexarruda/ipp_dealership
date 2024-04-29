from django.views.generic import ListView, DetailView
from .models import Motorcycle
from django.db.models import Q
from django.utils.decorators import method_decorator

# Create your views here.


class MotorcycleListView(ListView):
    model = Motorcycle
    template_name = 'motorcycles/motorcycle_list.html'
    context_object_name = 'motorcycle_list'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(model__icontains=search) |
                Q(manufacturer__name__icontains=search) |
                Q(engine_size__icontains=search)
            )
        return queryset


class MotorcycleDetailView(DetailView):
    model = Motorcycle
    template_name = 'motorcycles/motorcycle_detail.html'
    context_object_name = 'motorcycle_detail'
