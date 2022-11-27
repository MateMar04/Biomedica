import datetime
import random
import string

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


def get_paciente_for_resultado_view(request):
    pacientes = Paciente.objects.all()
    return render(request, "get_resultado.html", context={"paciente": pacientes})


def get_paciente_for_resultado(request):
    pacientes = Paciente.objects.all()
    paciente = pacientes[int(request.POST['paciente']) - 1]
    return render(request, "resultado.html", context={"paciente": paciente})


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


def registrar_solicitud(request, null=None):
    print(f"---{request.POST}---")

    pacientes = Paciente.objects.all()
    medicos = Medico.objects.all()
    estados = EstadoDeSolicitud.objects.all()
    estudios = Estudio.objects.all()
    extraccionistas = Extraccionista.objects.all()
    print(f"+++{estados}+++")
    print(f"+++{estados[2]}+++")

    solicitud = Solicitud.objects.create(receta=request.POST['receta'],
                                         id_paciente=pacientes[int(request.POST['paciente']) - 1],
                                         id_estado=estados[2],
                                         id_medico=medicos[int(request.POST['medico']) - 1],
                                         id_extraccionista=extraccionistas[int(request.POST['extraccionista']) - 1],
                                         fecha_hora_inicio=datetime.datetime.now(), fecha_hora_finalizacion=null,
                                         cap=generate_cap(8))

    print(request.POST.getlist('estudio'))
    for i in range(len(request.POST.getlist('estudio'))):
        resultado = Resultado.objects.create(valor_hallado=null, fecha=null,
                                             id_estudio=estudios[int(request.POST.getlist('estudio')[i]) - 1],
                                             id_solicitud=solicitud, observacion=null)

    return render(request, "success_solicitud.html")


def generate_cap(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
