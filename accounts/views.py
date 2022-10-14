from django.shortcuts import render, redirect
from .models import User
from .forms import CustomUserCreationForm

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
