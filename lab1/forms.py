
from django import forms
from .models import (
    Tovar,
    Postavchik,
    Clienti,
    Cotrudniki,
    Zakazi
)

class TovarForm(forms.ModelForm):
    class Meta:
        model = Tovar
        fields = '__all__'


class PostavchikForm(forms.ModelForm):
    class Meta:
        model = Postavchik
        fields = '__all__'


class ClientiForm(forms.ModelForm):
    class Meta:
        model = Clienti
        fields = '__all__'


class CotrudnikiForm(forms.ModelForm):
    class Meta:
        model = Cotrudniki
        fields = '__all__'


class ZakaziForm(forms.ModelForm):
    class Meta:
        model = Zakazi
        fields = '__all__'
