from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login
from .models import UserDB

# Create your views here.


def index(request):
    return render(request, 'authentication/index.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'authentication/register.html', context)


def login(request):

    # if request.method == "POST":
    #     form = LoginForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data["username"]
    #         password = form.cleaned_data["password"]
    #
    #         user = authenticate(request, username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #         else:
    #             print('Wrong credentials')
    # else:
    form = LoginForm()
    context = {'form': form}
    return render(request, 'authentication/login.html', context)


def logout(request):
    logout(request)
