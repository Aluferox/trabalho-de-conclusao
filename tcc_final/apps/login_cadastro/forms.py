from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CreateUsers(UserCreationForm):

    username = forms.CharField(
        label='',
        max_length=155,
        strip=True,
        help_text='',
        widget=forms.TextInput(attrs={'placeholder': 'Username'})

    )
    email = forms.EmailField(
        label='',
        max_length=255,
        required=True,
        help_text='',
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Entre com E-mail Válido.'
            }
        )
    )
    password1 = forms.CharField(
        label='',
        strip=False,
        help_text='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Dígite Sua Senha'})
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Repita a Senha'}),
        strip=False,
        help_text=_(""),
    )

    class Meta:
        model = User
        fields = ['username']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise ValidationError(
                _('Usuário Já Existe.'),
            )
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                _('Senhas Diferentes.')
            )
        return password2

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise ValidationError(
                _('Email Já Cadastrado.')
            )
