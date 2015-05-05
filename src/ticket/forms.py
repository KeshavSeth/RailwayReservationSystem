from django import forms
from django.utils.translation import gettext_lazy as _


class PassengerForm(forms.Form):
    name = forms.CharField(label="Name")
    age = forms.IntegerField(label="Age")
    sex = forms.CharField(label="Sex")
    birthPreference = forms.CharField(label="Birth Preference")
    foodPreference = forms.CharField(label="Food Preference")
    senior = forms.BooleanField(label="Senior Citizen", required=False)
