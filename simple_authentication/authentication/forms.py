from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User
from .models import CustomUser
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
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


# cant use below, because it took validation from Customer User
# username = unique!
# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ['username', 'password']
#         widgets = {
#             'password': forms.PasswordInput()
#         }
#         labels = {
#             'username': 'Your username',
#             'password': 'some password'
#         }

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
