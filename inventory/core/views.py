""" 
The views modules: to dictate what content will be rendered on the frontend
"""
from django.shortcuts import render

# Create your views here.
def index(request):
    """ the landing page """
    return render(request, "core/index.html")

def about(request):
    """ About me """
    return render(request, "core/about.html")

def contact(request):
    """ my contact page """
    return render(request, "core/about.html")
def login(request):
    """ my contact page """
    return render(request, "core/login.html")

def signup(request):
    """ my contact page """
    return render(request, "core/signup.html")
