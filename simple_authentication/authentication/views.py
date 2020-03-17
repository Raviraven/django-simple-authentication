from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm

# Create your views here.


def register(request):
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'authentication/register.html', context)


def login(request):
    form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})
