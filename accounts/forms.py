from django import forms
from django.core.exceptions import ValidationError
from django.forms import PasswordInput

from accounts.models import User


def check_email(value):
    value_list = list(value)
    if len(value_list) < 6 or '@' not in value_list:
        raise ValidationError('Incorrect email address')
    else:
        return True


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=64, validators=[check_email], label='E-mail', required=True)
    password = forms.CharField(max_length=32, widget=PasswordInput(), label='Password', required=True)


class CreateUserForm(forms.ModelForm):
    password1 = forms.CharField(label='Input password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Retype password', widget=forms.PasswordInput())

    def clean(self):
        data = super().clean()
        password1 = data.get('password1', '')
        password2 = data.get('password2', '')
        if password1 != password2:
            raise ValidationError('Passwords must be identical!')
        else:
            return data


