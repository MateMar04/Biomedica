from django.shortcuts import render


def home_screen_view(request):
    return render(request, "index.html")


def login_screen_view(request):
    return render(request, "login.html")
