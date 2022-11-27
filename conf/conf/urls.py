"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from confApp.views import (
    home_screen_view,
    paciente_screen_view,
    solicitud_screen_view,
    resultado_screen_view,
    medico_screen_view,
    registrar_medico,
    registrar_paciente,
    registrar_solicitud,
    get_paciente_for_resultado,
    get_paciente_for_resultado_view,
    get_paciente_for_modificacion_view,
    modify_paciente
)
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
    path('paciente_register/', paciente_screen_view, name='paciente'),
    path('solicitud_register/', solicitud_screen_view, name='solicitud'),
    path('resultado/', resultado_screen_view, name='resultado'),
    path('medico_register/', medico_screen_view, name='medico'),
    path('success_medico/', registrar_medico, name='registrarMedico'),
    path('success_paciente/', registrar_paciente, name='registrarPaciente'),
    path('success_solicitud/', registrar_solicitud, name='registrarSolicitud'),
    path('get_paciente_for_resultado/', get_paciente_for_resultado, name='getPacienteForResultado'),
    path('get_paciente_for_resultado_view/', get_paciente_for_resultado_view, name='getPacienteForResultadoView'),
    path('get_paciente_for_modificacion_view/', get_paciente_for_modificacion_view,
         name='getPacienteForModificacionView'),
    path('modify_paciente/', modify_paciente, name='modifyPaciente')
]
