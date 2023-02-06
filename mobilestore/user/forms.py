from django import forms
from account.models import User
from .models import Purchase,FeedbackModel
class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"

class PurchaseForm(forms.ModelForm):
    class Meta:
        model=Purchase
        fields=['quantity'
        ]
        widgets={
            'quantity':forms.NumberInput(attrs={'placeholder':'Enter quanity','class':'form-control'}),
           
        }
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=FeedbackModel
        fields=['feedback']
        widgets={'feedback':forms.Textarea(attrs={'class':'form-control'})
        }
       

