from datetime import datetime
from django import forms
from .models import Motorcycle


class MotorcycleModelForm(forms.ModelForm):
    class Meta:
        model = Motorcycle
        fields = '__all__'

    def clean_year(self):
        year = self.cleaned_data['year']
        if year < 1970 or year > datetime.now().year:
            raise forms.ValidationError('Invalid year')
        return year

    def clean_engine_size(self):
        engine_size = self.cleaned_data['engine_size']
        if engine_size < 50 or engine_size > 2500:
            raise forms.ValidationError('Invalid engine size')
        return engine_size

    def clean_price(self):
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Invalid price')
        return price
