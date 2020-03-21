from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from .models import CustomUser

# Create your views here.


def index(request):
    return render(request, 'authentication/index.html')


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)


def login_user(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request=request, user=user)
                return redirect(settings.LOGIN_REDIRECT_URL)
            else:
                credentials_error = 'Invalid username or password'
                form.add_error(None, credentials_error)
    else:
        form = LoginForm()
    context = {'form': form}
    return render(request, 'authentication/login.html', context)


def logout_user(request):
    logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
