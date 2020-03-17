from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegisterForm, LoginForm
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
    form = LoginForm()
    return render(request, 'authentication/login.html', {'form': form})
