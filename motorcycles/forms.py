from datetime import datetime
from django import forms
from .models import Motorcycle


class MotorcycleModelForm(forms.ModelForm):
    class Meta:
        model = Motorcycle
        fields = "__all__"

    def clean_production_year(self):
        production_year = self.cleaned_data["production_year"]
        if production_year < 1970 or production_year > datetime.now().year:
            raise forms.ValidationError("Invalid year")
        return production_year

    def clean_model_year(self):
        model_year = self.cleaned_data["model_year"]
        if model_year < 1970 or model_year > datetime.now().year:
            raise forms.ValidationError("Invalid year")
        return model_year

    def clean_engine_size(self):
        engine_size = self.cleaned_data["engine_size"]
        if engine_size < 50 or engine_size > 2500:
            raise forms.ValidationError("Invalid engine size")
        return engine_size

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price < 0:
            raise forms.ValidationError("Invalid price")
        return price

    def clean_kilometrage(self):
        kilometrage = self.cleaned_data["kilometrage"]
        if kilometrage < 0:
            raise forms.ValidationError("Invalid kilometrage")
        return kilometrage
