from django.shortcuts import render, redirect
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    return render(request, "accounts/index.html")


def signup(request):
    if request.method == "POST":
        account_form = CustomUserCreationForm(request.POST)
        if account_form.is_valid():
            account_form.save()
            return redirect("accounts:index")
    else:
        account_form = CustomUserCreationForm()
    context = {"account_form": account_form}
    return render(request, "accounts/signup.html", context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("accounts:index")
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')