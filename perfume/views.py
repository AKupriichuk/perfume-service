from django.shortcuts import render
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

    return render(request, "perfume/perfume_list.html", context=context)