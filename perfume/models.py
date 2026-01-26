from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Perfume(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    def __str__(self):
        return self.name


class Perfumer(models.Model):
    perfume = models.ManyToManyField(Perfume)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    experience_years = models.IntegerField()
    perfumes = models.CharField(max_length=120)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Customer(AbstractUser):
    favourite_scent_family = models.CharField(max_length=400)

    def __str__(self):
        return self.first_name