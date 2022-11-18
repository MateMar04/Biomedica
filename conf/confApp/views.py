from django.shortcuts import render


def home_screen_view(request):
    return render(request, "index.html")


def login_screen_view(request):
    return render(request, "login.html")


def solicitud_screen_view(request):
    return render(request, "make_solicitud.html")


def resultado_screen_view(request):
    return render(request, "resultado.html")
