from django import forms
from account.models import User
from .models import Products


class StoreForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"
        

class Productform(forms.ModelForm):
    class Meta:
        model=Products
        fields="__all__"
        