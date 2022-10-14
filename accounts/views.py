from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
    return render(request, "accounts/main.html")


def index(request):
    account_list = get_user_model().objects.order_by("-id")

    context = {"account_list": account_list}
    return render(request, "accounts/index.html", context)


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
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("accounts:index")
    else:
        form = AuthenticationForm()
    context = {"form": form}
    return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("accounts:main")


@login_required
def detail(request, pk):
    account_detail = get_user_model().objects.get(pk=pk)

    context = {"account_detail": account_detail}

    return render(request, "accounts/detail.html", context)


@login_required
def update(request, pk):
    if request.user.pk == pk:
        if request.method == "POST":
            update_form = CustomUserChangeForm(request.POST, instance=request.user)
            if update_form.is_valid():
                update_form.save()
                return redirect("accounts:detail", request.user.pk)
        else:
            update_form = CustomUserChangeForm(instance=request.user)
        context = {"update_form": update_form}
        return render(request, "accounts/update.html", context)
    else:
        return render(request, 'accounts/diff.html')

def diff(request):
    return render(request, 'accounts/diff.html')