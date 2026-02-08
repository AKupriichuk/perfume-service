from django import forms
from django.core.exceptions import ValidationError
from .models import Perfumer, Perfume


class PerfumerForm(forms.ModelForm):
    class Meta:
        model = Perfumer
        fields = ["first_name", "last_name", "experience_years", "perfume"]

    def clean_experience_years(self):
        experience = self.cleaned_data.get("experience_years")

        if experience < 0:
            raise ValidationError("Стаж не може бути від'ємним чилом.")

        if experience > 70:
            raise ValidationError("Стаж не може перевищувати 70 років. Ви впевнені, що це не помилка?")

        return experience

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")
        if any(char.isdigit() for char in first_name):
            raise ValidationError("Ім'я не може містити цифри.")
        return first_name

class PerfumerLastNameSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Пошук за прізвищем..."})
    )