from django.shortcuts import render


def home_screen_view(request):
    return render(request, "index.html")


def paciente_screen_view(request):
    return render(request, "create_paciente.html")


def solicitud_screen_view(request):
    return render(request, "create_solicitud.html")


def resultado_screen_view(request):
    return render(request, "resultado.html")


def medico_screen_view(request):
    return render(request, "create_medico.html")
