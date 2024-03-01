from django.shortcuts import render


def landing(request):
    return render(request, 'users/landing.html')


def login(request):
    return render(request, 'users/login.html')


def register(request):
    return render(request, 'users/register.html')