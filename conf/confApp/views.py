from django.shortcuts import render

from .models import Medico, TipoDeDocumento, Sexo, Paciente, Domicilio


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


def registrar_paciente(request):
    print(f"---{request.POST}---")
    #domicilio = Domicilio.objects.create(calle=request.POST['calle'], altura=request.POST['altura'],
    #                                     n_piso=request.POST['nro_piso'], departamento=request.POST['departamento'])
    #paciente = Paciente.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
    #                                   id_tipo_de_documento=request.POST['tipo_documento'],
    #                                   n_documento=request.POST['nro_documento'], id_sexo=request.POST['sexo'],
    #                                   id_domicilio=domicilio.id, telefono=request.POST['telefono'],
    #                                   email=request.POST['email'])
    return render(request, "succesfull.html")
