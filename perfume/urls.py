from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path("", index),
    path('perfume/', views.PerfumeListView.as_view(), name='perfumes'),
    path('manufacturers/', views.ManufacturerListView.as_view(), name='manufacturers'),
    path('perfume/<int:pk>/', views.PerfumeDetailView.as_view(), name='perfume_detail'),
]