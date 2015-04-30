from django import forms
from datetime import datetime


class SearchForm(forms.Form):
    source = forms.CharField(label='From', max_length=255)
    destination = forms.CharField(label='To', max_length=255)
    date = forms.DateField(
        label="Date of journey")
