from django.urls import path
from . import views

app_name = "perfume"

urlpatterns = [
    path("", views.index, name="index"),
    path('perfume/', views.PerfumeListView.as_view(), name='perfumes'),
    path('manufacturer/', views.ManufacturerListView.as_view(), name='manufacturers'),
    path('manufacturer/<int:pk>/', views.ManufacturerDetailView.as_view(), name='manufacturer_detail'),
    path('perfume/<int:pk>/', views.PerfumeDetailView.as_view(), name='perfume_detail'),
    path('perfumer/', views.PerfumerListView.as_view(), name='perfumers'),
    path('perfumer/<int:pk>/', views.PerfumerDetailView.as_view(), name='perfumer_detail'),

    path("perfumes/create/", views.PerfumeCreateView.as_view(), name="perfume-create"),
    path("perfumes/<int:pk>/update/", views.PerfumeUpdateView.as_view(), name="perfume-update"),
    path("perfumes/<int:pk>/delete/", views.PerfumeDeleteView.as_view(), name="perfume-delete"),

    path("perfumers/create/", views.PerfumerCreateView.as_view(), name="perfumer-create"),
    path("perfumers/<int:pk>/update/", views.PerfumerUpdateView.as_view(), name="perfumer-update"),
    path("perfumers/<int:pk>/delete/", views.PerfumerDeleteView.as_view(), name="perfumer-delete"),

    path("manufacturers/create/", views.ManufacturerCreateView.as_view(), name="manufacturer-create"),
    path("manufacturers/<int:pk>/update/", views.ManufacturerUpdateView.as_view(), name="manufacturer-update"),
    path("manufacturers/<int:pk>/delete/", views.ManufacturerDeleteView.as_view(), name="manufacturer-delete"),
]
