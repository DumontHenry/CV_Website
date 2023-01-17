from django import forms
from .models import *
from django.core.validators import RegexValidator


# https://stackoverflow.com/questions/5827590/css-styling-in-django-forms

my_validator = RegexValidator(r'^\+?1?\d{9,15}$', "Your string should contain numbers in it.")


class ContactForm(forms.ModelForm):
    phone = forms.CharField(required=True, validators=[my_validator], widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'message', 'placeholder': 'Enter your phone number...',
               'type': 'tel', }))
    name = forms.CharField(required=True,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter your name...',
                                      'type': 'text'}))
    message = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'message', 'placeholder': 'Enter your message...',
               'type': 'text'}))
    email = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'Enter your email...',
               'type': 'email'}))

    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']


class PDFForm(forms.ModelForm):
    class Meta:
        model = PDF
        fields = ['author', 'title', 'file']

