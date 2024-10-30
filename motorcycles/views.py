from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
    CreateView,
)
from motorcycles.forms import MotorcycleModelForm
from .models import Motorcycle
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


class MotorcycleListView(ListView):
    model = Motorcycle
    template_name = "motorcycles/motorcycle_list.html"
    context_object_name = "motorcycle_list"
    paginate_by = 12

    def get_queryset(self):
        queryset = super().get_queryset().order_by("model")
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                Q(model__icontains=search)
                | Q(manufacturer__name__icontains=search)
                | Q(engine_size__icontains=search)
            )
        return queryset


class MotorcycleDetailView(DetailView):
    model = Motorcycle
    template_name = "motorcycles/motorcycle_detail.html"
    context_object_name = "motorcycle_detail"


@method_decorator(staff_member_required, name="dispatch")
class MotorcycleUpdateView(UpdateView):
    model = Motorcycle
    form_class = MotorcycleModelForm
    template_name = "motorcycles/motorcycle_update.html"

    def get_success_url(self):
        return reverse_lazy("motorcycle_detail", kwargs={"pk": self.object.pk})


@method_decorator(staff_member_required, name="dispatch")
class MotorcycleDeleteView(DeleteView):
    model = Motorcycle
    template_name = "motorcycles/motorcycle_delete.html"
    success_url = reverse_lazy("motorcycle_list")


@method_decorator(staff_member_required, name="dispatch")
class MotorcycleCreateView(CreateView):
    model = Motorcycle
    form_class = MotorcycleModelForm
    template_name = "motorcycles/motorcycle_create.html"

    def get_success_url(self):
        return reverse_lazy("motorcycle_detail", kwargs={"pk": self.object.pk})
