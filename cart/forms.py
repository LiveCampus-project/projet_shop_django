from django import forms
from .models import Articles, Delivery

class CartForm(forms.Form):
    articles = forms.ModelMultipleChoiceField(queryset=Articles.objects.all(), widget=forms.CheckboxSelectMultiple)
    delivery = forms.ModelChoiceField(queryset=Delivery.objects.all())
