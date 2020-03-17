from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
from .models import UserDB
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = UserDB
        fields = ['username', 'email', 'password1', 'password2', 'some_additional_property']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'my-test-class'}),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
            'some_additional_property': forms.TextInput()
        }
        labels = {
            'username': 'Your username',
            'some_additional_property': 'Additional property, change to w/e'
        }


class LoginForm(AuthenticationForm):
    class Meta:
        model = UserDB
        fields = ['username']
        labels = {
            'username': 'Your username',
            'password': 'some password'
        }