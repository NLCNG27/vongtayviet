from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def register_view(request):
    return render(request, '../templates/register.html')

def login_view(request):
    return render(request, '../templates/login.html')

