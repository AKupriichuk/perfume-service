from django.test import TestCase
from perfume.models import Perfumer

class ModelTests(TestCase):
    def test_perfumer_str(self):
        perfumer = Perfumer.objects.create(
            first_name="Francis",
            last_name="Kurkdjian",
            experience_years=25
        )
        # Перевіряємо, чи правильно працює __str__
        self.assertEqual(str(perfumer), "Francis Kurkdjian")