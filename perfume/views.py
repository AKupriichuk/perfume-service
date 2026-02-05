from django.http.response import HttpResponse
from django.urls.base import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import PerfumerForm, PerfumerLastNameSearchForm
from .models import Perfume, Manufacturer, Perfumer
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    num_perfumes = Perfume.objects.count()
    num_manufacturers = Manufacturer.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_perfumes": num_perfumes,
        "num_manufacturers": num_manufacturers,
        "num_visits": num_visits + 1,
    }

    return render(request, "perfume/index.html", context=context)


class PerfumeListView(LoginRequiredMixin, generic.ListView):
    model = Perfume
    context_object_name = "perfumes"
    queryset = Perfume.objects.select_related("manufacturer")
    template_name = "perfume/perfume_list.html"
    paginate_by = 3


class PerfumeCreateView(generic.CreateView):
    model = Perfume
    fields = "__all__"
    success_url = reverse_lazy("perfume:perfumes")
    template_name = "perfume/perfume_form.html"


class PerfumeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Perfume
    success_url = reverse_lazy("perfume:perfumes")
    template_name = "perfume/perfume_form.html"


class PerfumeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Perfume
    success_url = reverse_lazy("perfume:perfumes")
    template_name = "perfume/perfume_confirm_delete.html"


class PerfumeDetailView(generic.DetailView):
    model = Perfume


class PerfumerListView(LoginRequiredMixin, generic.ListView):
    model = Perfumer
    context_object_name = "perfumers"
    queryset = Perfumer.objects.prefetch_related('perfume')
    template_name = "perfume/perfumer_list.html"
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PerfumerListView, self).get_context_data(**kwargs)
        last_name = self.request.GET.get("last_name", "")
        context["search_form"] = PerfumerLastNameSearchForm(
            initial={"last_name": last_name}
        )
        return context

    def get_queryset(self):
        queryset = Perfumer.objects.all()
        last_name = self.request.GET.get("last_name")

        if last_name:
            return queryset.filter(last_name__icontains=last_name)
        return queryset


class PerfumerDetailView(generic.DetailView):
    model = Perfumer


class PerfumerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Perfumer
    form_class = PerfumerForm
    success_url = reverse_lazy("perfume:perfumers")
    template_name = "perfume/perfumer_form.html"

class PerfumerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Perfumer
    form_class = PerfumerForm
    success_url = reverse_lazy("perfume:perfumers")
    template_name = "perfume/perfumer_form.html"

class PerfumerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Perfumer
    success_url = reverse_lazy("perfume:perfumers")
    template_name = "perfume/perfumer_confirm_delete.html"

class ManufacturerListView(generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturers"
    queryset = Manufacturer.objects.all()
    template_name = "perfume/manufacturers_list.html"
    paginate_by = 3


class ManufacturerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("perfume:manufacturers")


class ManufacturerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("perfume:manufacturers")


class ManufacturerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("perfume:manufacturers")


class ManufacturerDetailView(generic.DetailView):
    model = Manufacturer
