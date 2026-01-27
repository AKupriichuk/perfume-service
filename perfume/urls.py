from django.urls import path
from .views import index

urlpatterns = [
    path("", index), # Порожні лапки означають головну сторінку
]