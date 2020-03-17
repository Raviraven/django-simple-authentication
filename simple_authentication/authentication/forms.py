from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'my-test-class'}),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput()
        }
        labels = {
            'username': 'Your username'
        }


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        labels = {
            'username': 'Your username'
        }