from django.shortcuts import render

from .models import *


def home_screen_view(request):
    return render(request, "index.html")


def paciente_screen_view(request):
    tipos_de_documentos = TipoDeDocumento.objects.all()
    sexos = Sexo.objects.all()
    return render(request, "create_paciente.html", context={"tipo": tipos_de_documentos, "sexo": sexos})


def solicitud_screen_view(request):
    pacientes = Paciente.objects.all()
    extraccionistas = Extraccionista.objects.all()
    medicos = Medico.objects.all()
    estudios = Estudio.objects.all()
    return render(request, "create_solicitud.html",
                  context={"paciente": pacientes, "extraccionista": extraccionistas, "medico": medicos,
                           "estudio": estudios})


def resultado_screen_view(request):
    return render(request, "resultado.html")


def medico_screen_view(request):
    return render(request, "create_medico.html")


def registrar_medico(request):
    print(f"---{request.POST}---")
    medico = Medico.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
                                   matricula=request.POST['matricula'])
    return render(request, "success_medico.html")


def registrar_paciente(request, null=None):
    print(f"---{request.POST}---")
    if request.POST['nro_piso'] == '':
        nro_piso = null

    if request.POST['departamento'] == '':
        departamento = null

    domicilio = Domicilio.objects.create(calle=request.POST['calle'], altura=request.POST['altura'],
                                         n_piso=nro_piso, departamento=departamento)
    tipo_de_documentos = TipoDeDocumento.objects.all()
    sexos = Sexo.objects.all()
    telefono = Telefono.objects.create(numero=request.POST['telefono'])
    paciente = Paciente.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
                                       id_tipo_de_documento=tipo_de_documentos[int(request.POST['tipo_documento']) - 1],
                                       n_documento=request.POST['nro_documento'],
                                       id_sexo=sexos[int(request.POST['sexo']) - 1], id_domicilio=domicilio,
                                       id_telefono=telefono, email=request.POST['email'])
    return render(request, "success_paciente.html")


def registrar_solicitud(request):
    print(f"---{request.POST}---")

    return render(request, "success_solicitud.html")
