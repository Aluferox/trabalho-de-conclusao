from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUsers(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
