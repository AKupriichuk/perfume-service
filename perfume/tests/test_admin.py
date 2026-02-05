from django.contrib.auth import get_user_model
from django.test.testcases import TestCase
from django.urls import reverse

from perfume.models import Perfumer


class AdminPanelTests(TestCase):
    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="password123"
        )
        self.client.force_login(self.admin_user)
        self.perfumer = Perfumer.objects.create(
            first_name="Jean", last_name="Claude", experience_years=40
        )

    def test_perfumer_list_display(self):
        url = reverse("admin:perfume_perfumer_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.perfumer.last_name)
