from django.http.response import HttpResponse
from django.views import generic
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Perfume, Manufacturer


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


class PerfumeListView(generic.ListView):
    model = Perfume
    context_object_name = "perfumes"
    queryset = Perfume.objects.select_related("manufacturer")
    template_name = "perfume/perfume_list.html"
    paginate_by = 3


class PerfumeDetailView(generic.DetailView):
    model = Perfume


class ManufacturerListView(generic.ListView):
    model = Manufacturer
    context_object_name = "manufacturers"
    queryset = Manufacturer.objects.all()
    template_name = "perfume/manufacturers_list.html"
    paginate_by = 3


def test_session_view(request):
    request.session["test"] = "test session"
    num_visits = request.session.get("num_visits", 0) + 1
    request.session["num_visits"] = num_visits
    return HttpResponse(
        f"<h1>Session data: {request.session['test']}</h1>"
        f"You have visited this page {num_visits} times"
    )
