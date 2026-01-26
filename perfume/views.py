from django.shortcuts import render
from .models import Perfume


def perfume_list(request):
    perfumes = Perfume.objects.all()

    return render(request, 'perfume/perfume_list.html', {'perfumes': perfumes})

