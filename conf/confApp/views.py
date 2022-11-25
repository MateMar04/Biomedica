from django.shortcuts import render

from .models import Medico, TipoDeDocumento, Sexo


def home_screen_view(request):
    return render(request, "index.html")


def paciente_screen_view(request):
    tipos_de_documentos = TipoDeDocumento.objects.all()
    sexos = Sexo.objects.all()
    return render(request, "create_paciente.html", context={"tipo": tipos_de_documentos, "sexo": sexos})


def solicitud_screen_view(request):
    return render(request, "create_solicitud.html")


def resultado_screen_view(request):
    return render(request, "resultado.html")


def medico_screen_view(request):
    return render(request, "create_medico.html")


def registrar_medico(request):
    print(f"---{request.POST}---")
    medico = Medico.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
                                   matricula=request.POST['matricula'])
    return render(request, "succesfull.html")
