""" 
The views modules: to dictate what content will be rendered on the frontend
"""
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.hashers import make_password
from .models import Product, CustomUser, Supplier, Stock
from .forms import LoginForm, SignUpForm
import requests as req
from django.template import loader
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect('home')
    return render(request, 'delete_account.html')

def index(request):
    """ the landing page """
    prod_list = Product.objects.all()
    template = loader.get_template("core/index.html")
    context = {
            "prod_list": prod_list,
            }
    return render(request, "core/index.html", context)

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')


def about(request):
    """ About me """
    return render(request, "core/about.html")

def contact(request):
    """ my contact page """
    return render(request, "core/about.html")

class CustomLoginView(LoginView):
    template_name = "core/login.html"
    authentication_form = LoginForm
#    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('core:dashboard')




class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('core:login')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('core/new_product.html')
    else:
        form = SignUpForm()
    return render(request, "core/signup.html", {"form": form})

def new_product(request):
    """ creation of a new product instance """
    return render(request, "core/new_product.html")

def edit_product(request):
    """ Edit an existing product """
    return render(request, "core/edit_product.html")
