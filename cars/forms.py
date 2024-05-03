from datetime import datetime
from django import forms
from .models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_production_year(self):
        production_year = self.cleaned_data['production_year']
        if production_year < 1970 or production_year > datetime.now().year:
            raise forms.ValidationError('Invalid year')
        return production_year

    def clean_model_year(self):
        model_year = self.cleaned_data['model_year']
        if model_year < 1970 or model_year > datetime.now().year:
            raise forms.ValidationError('Invalid year')
        return model_year

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Invalid price')
        return price

    def clean_doors(self):
        doors = self.cleaned_data['doors']
        if doors < 1 or doors > 6:
            raise forms.ValidationError('Invalid number of doors')
        return doors

    def clean_kilometrage(self):
        kilometrage = self.cleaned_data['kilometrage']
        if kilometrage < 0:
            raise forms.ValidationError('Invalid kilometrage')
        return kilometrage
