from django.contrib.auth import get_user_model
from django.test.testcases import TestCase
from django.urls.base import reverse


class PrivateViewTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="password123"
        )
        self.client.force_login(self.user)

    def test_retrieve_perfumers_list(self):
        url = reverse("perfume:perfumers")
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "perfume/perfumer_list.html")