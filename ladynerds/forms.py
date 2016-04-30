from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import User


class UserForm(ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(ModelForm):
    class Meta:
        model = User
        exclude = ['password']

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )