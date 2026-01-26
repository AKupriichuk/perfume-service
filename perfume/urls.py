from django.urls import path
from .views import perfume_list

urlpatterns = [
    path("catalog/perfumes/", perfume_list, name="index"), # Порожні лапки означають головну сторінку
]