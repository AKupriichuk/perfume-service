from django.urls import path
from . import views

app_name = "perfume"

urlpatterns = [
    path("", views.index, name="index"),
    path('perfume/', views.PerfumeListView.as_view(), name='perfumes'),
    path('manufacturer/', views.ManufacturerListView.as_view(), name='manufacturers'),
    path('perfume/<int:pk>/', views.PerfumeDetailView.as_view(), name='perfume_detail'),
]