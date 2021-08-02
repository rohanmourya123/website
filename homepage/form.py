from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Contact,login

class signup_form(UserCreationForm):
    class Meta:
        model=User
        fields= ("username","password1","password2","email")

class contact_form(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"

class login_form(forms.ModelForm):
    class Meta:
        model=login
        fields="__all__"