import datetime
import io
import random
import string

from django.http import FileResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas

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
    solicitudes = Solicitud.objects.filter(id_paciente=paciente.id)
    resultados = Resultado.objects.filter(id_solicitud__id_paciente=paciente)

    return render(request, "resultado.html",
                  context={"paciente": paciente, "solicitud": solicitudes, "resultado": resultados})


def get_paciente_for_modificacion_view(request):
    pacientes = Paciente.objects.all()
    return render(request, "get_modificacion.html", context={"paciente": pacientes})


def load_paciente(request):
    pacientes = Paciente.objects.all()
    tipos_de_documentos = TipoDeDocumento.objects.all()
    sexos = Sexo.objects.all()

    paciente = pacientes[int(request.POST['paciente']) - 1]
    domicilio = Domicilio.objects.filter(id=paciente.id_domicilio.id)
    telefono = Telefono.objects.filter(id=paciente.id_telefono.id)

    return render(request, "modify_paciente.html",
                  context={"paciente": paciente, "tipo": tipos_de_documentos, "sexo": sexos})


def modify_paciente(request, null=None):
    try:
        pacientes = Paciente.objects.all()
        paciente = pacientes[int(request.POST['id']) - 1]
        tipos_de_documentos = TipoDeDocumento.objects.all()
        sexos = Sexo.objects.all()

        Telefono.objects.filter(id=paciente.id_telefono.id).update(numero=request.POST['telefono'])

        Domicilio.objects.filter(id=paciente.id_domicilio.id).update(calle=request.POST['calle'],
                                                                     altura=request.POST['altura'],
                                                                     n_piso=0 if request.POST[
                                                                                     'nro_piso'] is null or 'None' or '' else
                                                                     int(request.POST['nro_piso']),
                                                                     departamento='' if request.POST[
                                                                                            'departamento'] is null or 'None' else
                                                                     request.POST['departamento'])

        Paciente.objects.filter(id=paciente.id).update(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
                                                       id_tipo_de_documento=tipos_de_documentos[
                                                           int(request.POST['tipo_documento']) - 1],
                                                       n_documento=request.POST['nro_documento'],
                                                       id_sexo=sexos[int(request.POST['sexo']) - 1],
                                                       email=request.POST['email'])

        message = f"Paciente {paciente} modificado con exito"
        return render(request, "success.html", context={"message": message})
    except:
        message = f"El Paciente no se pudo modificar"
        return render(request, "failed.html", context={"message": message})


def medico_screen_view(request):
    return render(request, "create_medico.html")


def registrar_medico(request):
    try:
        medico = Medico.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
                                       matricula=request.POST['matricula'])
        message = f"Medico {medico} registrado con exito"
        return render(request, "success.html", context={"message": message})
    except:
        message = f"El Medico no se pudo registrar"
        return render(request, "failed.html", context={"message": message})


def registrar_paciente(request, null=None):
    try:
        if request.POST['nro_piso'] == '' or null:
            nro_piso = 0

        if request.POST['departamento'] == '' or null:
            departamento = '-'

        domicilio = Domicilio.objects.create(calle=request.POST['calle'], altura=request.POST['altura'],
                                             n_piso=nro_piso, departamento=departamento)
        tipo_de_documentos = TipoDeDocumento.objects.all()
        sexos = Sexo.objects.all()
        telefono = Telefono.objects.create(numero=request.POST['telefono'])
        paciente = Paciente.objects.create(nombre=request.POST['nombre'], apellido=request.POST['apellido'],
                                           id_tipo_de_documento=tipo_de_documentos[
                                               int(request.POST['tipo_documento']) - 1],
                                           n_documento=request.POST['nro_documento'],
                                           id_sexo=sexos[int(request.POST['sexo']) - 1], id_domicilio=domicilio,
                                           id_telefono=telefono, email=request.POST['email'])
        message = f"Paciente {paciente} registrado con exito"
        return render(request, "success.html", context={"message": message})
    except:
        message = f"El Paciente no se pudo registrar"
        return render(request, "failed.html", context={"message": message})


def registrar_solicitud(request, null=None):
    limit_date = datetime.date.today() - datetime.timedelta(days=15)
    try:
        if request.POST['fecha_receta'] > str(limit_date):

            buffer = io.BytesIO()
            p = canvas.Canvas(buffer)

            pacientes = Paciente.objects.all()
            medicos = Medico.objects.all()
            estados = EstadoDeSolicitud.objects.all()
            estudios = Estudio.objects.all()
            extraccionistas = Extraccionista.objects.all()
            solicitud = Solicitud.objects.create(receta=request.POST['receta'],
                                                 fecha_receta=request.POST['fecha_receta'],
                                                 id_paciente=pacientes[int(request.POST['paciente']) - 1],
                                                 id_estado=estados[2],
                                                 id_medico=medicos[int(request.POST['medico']) - 1],
                                                 id_extraccionista=extraccionistas[
                                                     int(request.POST['extraccionista']) - 1],
                                                 fecha_hora_inicio=datetime.datetime.now(),
                                                 fecha_hora_finalizacion=null,
                                                 cap=generate_cap(8))

            p.drawString(100, 800, f"BIOMEDICA")
            p.drawString(100, 760, f"Solicitud ID: {solicitud.id}")
            p.drawString(100, 740, f"Fecha: {solicitud.fecha_hora_inicio}")
            p.drawString(100, 720,
                         f"Extraccionista: {solicitud.id_extraccionista.nombre} {solicitud.id_extraccionista.apellido}")
            p.drawString(100, 680, f"Paciente: {solicitud.id_paciente.nombre} {solicitud.id_paciente.apellido}")
            p.drawString(100, 660, f"Medico: {solicitud.id_medico.nombre} {solicitud.id_medico.apellido}")
            p.drawString(100, 620, "Estudios")
            altura = 620
            for i in range(len(request.POST.getlist('estudio'))):
                resultado = Resultado.objects.create(valor_hallado=null, fecha=null,
                                                     id_estudio=estudios[int(request.POST.getlist('estudio')[i]) - 1],
                                                     id_solicitud=solicitud, observacion=null)
                altura = altura - 20
                p.drawString(110, altura, f"* {resultado.id_estudio.nombre}")

            p.drawString(100, altura - 40, f"CAP: {solicitud.cap}")

            p.showPage()
            p.save()
            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename='comprobante_solicitud.pdf')
        else:
            message = f"La solicitud no se pudo registrar porque la receta esta vencida"
            return render(request, "failed.html", context={"message": message})
    except:
        message = f"La solicitud no se pudo registrar"
        return render(request, "failed.html", context={"message": message})


def generate_cap(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def generate_pdf(text):
    pass
