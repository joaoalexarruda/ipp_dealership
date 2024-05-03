from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .forms import CarModelForm
from .models import Car
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


class CarListView(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    context_object_name = 'car_list'
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(model__icontains=search) |
                Q(brand__name__icontains=search) |
                Q(engine_size__icontains=search)
            )
        return queryset


class CarDetailView(DetailView):
    model = Car
    template_name = 'cars/car_detail.html'
    context_object_name = 'car_detail'


@method_decorator(staff_member_required, name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'cars/car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


@method_decorator(staff_member_required, name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'cars/car_delete.html'
    success_url = reverse_lazy('car_list')


@method_decorator(staff_member_required, name='dispatch')
class CarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'cars/car_create.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})
