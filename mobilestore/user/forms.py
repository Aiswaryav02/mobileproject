from django import forms
from account.models import User

class UseProForm(forms.ModelForm):
    class Meta:
        model=User
