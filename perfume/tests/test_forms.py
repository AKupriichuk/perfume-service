from django.test.testcases import TestCase

from perfume.forms import PerfumerForm

class FormTests(TestCase):
    def test_perfumer_form_invalid_experience(self):
        form_data = {
            "first_name": "Francis",
            "last_name": "Kurkdjian",
            "experience_years": -5,
        }
        form = PerfumerForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_perfumer_form_invalid_name(self):
        form_data = {
            "first_name": "Francis123",
            "last_name": "Kurkdjian",
            "experience_years": 10,
        }
        form = PerfumerForm(data=form_data)
        self.assertFalse(form.is_valid())