from django import forms

class MarcarPalabraForm(forms.Form):
    palabra = forms.CharField(max_length=100)