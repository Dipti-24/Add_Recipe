from django import forms
from .models import*

class MyModel2(forms.Form):
   color = forms.CharField(widget=forms.Select)