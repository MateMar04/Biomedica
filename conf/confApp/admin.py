from django.contrib import admin
from .models import Medico
from .models import Domicilio
from .models import EstadoDeSolicitud
from .models import Estudio
from .models import Extraccionista
from .models import Metodo
from .models import Muestra
from .models import Paciente
from .models import Resultado
from .models import Sexo
from .models import Solicitud
from .models import Telefono
from .models import TipoDeDocumento
from .models import UnidadDeMedida


class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'matricula',)
    search_fields = ('id', 'nombre', 'apellido', 'matricula',)
    list_filter = ('id', 'nombre', 'apellido', 'matricula',)
    list_per_page = 10


class DomicilioAdmin(admin.ModelAdmin):
    list_display = ('id', 'calle', 'altura', 'n_piso', 'departamento',)
    search_fields = ('id', 'calle', 'altura', 'n_piso', 'departamento',)
    list_filter = ('id', 'calle', 'altura', 'n_piso', 'departamento',)
    list_per_page = 10


class EstadoDeSolicitudAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripccion',)
    search_fields = ('id', 'nombre', 'descripccion',)
    list_filter = ('id', 'nombre', 'descripccion',)
    list_per_page = 10


class EstudioAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nombre', 'descripccion', 'limite_inferior', 'limite_superior', 'id_metodo', 'id_unidad_de_medida',)
    search_fields = (
        'id', 'nombre', 'descripccion', 'limite_inferior', 'limite_superior', 'id_metodo', 'id_unidad_de_medida',)
    list_filter = (
        'id', 'nombre', 'descripccion', 'limite_inferior', 'limite_superior', 'id_metodo', 'id_unidad_de_medida',)
    list_per_page = 10


class ExtraccionistaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido',)
    search_fields = ('id', 'nombre', 'apellido',)
    list_filter = ('id', 'nombre', 'apellido',)
    list_per_page = 10


class MedicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'matricula', 'nombre', 'apellido',)
    search_fields = ('id', 'matricula', 'nombre', 'apellido',)
    list_filter = ('id', 'matricula', 'nombre', 'apellido',)
    list_per_page = 10


class MetodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripccion',)
    search_fields = ('id', 'nombre', 'descripccion',)
    list_filter = ('id', 'nombre', 'descripccion',)
    list_per_page = 10


class MuestraAdmin(admin.ModelAdmin):
    list_display = ('id', 'descripccion', 'fecha_hora_extraccion', 'id_resultado',)
    search_fields = ('id', 'descripccion', 'fecha_hora_extraccion', 'id_resultado',)
    list_filter = ('id', 'descripccion', 'fecha_hora_extraccion', 'id_resultado',)
    list_per_page = 10


class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'n_documento', 'nombre', 'apellido', 'id_sexo', 'id_domicilio', 'id_telefono', 'id_tipo_de_documento',
        'email', 'contraseña',)
    search_fields = (
        'id', 'n_documento', 'nombre', 'apellido', 'id_sexo', 'id_domicilio', 'id_telefono', 'id_tipo_de_documento',
        'email', 'contraseña',)
    list_filter = (
        'id', 'n_documento', 'nombre', 'apellido', 'id_sexo', 'id_domicilio', 'id_telefono', 'id_tipo_de_documento',
        'email', 'contraseña',)
    list_per_page = 10


class ResultadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'valor_hallado', 'fecha', 'id_estudio', 'observacion',)
    search_fields = ('id', 'valor_hallado', 'fecha', 'id_estudio', 'observacion',)
    list_filter = ('id', 'valor_hallado', 'fecha', 'id_estudio', 'observacion',)
    list_per_page = 10


class SexoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripccion',)
    search_fields = ('id', 'nombre', 'descripccion',)
    list_filter = ('id', 'nombre', 'descripccion',)
    list_per_page = 10


class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('id', 'receta', 'id_paciente', 'id_extraccionista', 'id_estado', 'id_medico', 'fecha_hora_inicio',
                    'fecha_hora_finalizacion', 'cap')
    search_fields = ('id', 'receta', 'id_paciente', 'id_extraccionista', 'id_estado', 'id_medico', 'fecha_hora_inicio',
                     'fecha_hora_finalizacion', 'cap')
    list_filter = ('id', 'receta', 'id_paciente', 'id_extraccionista', 'id_estado', 'id_medico', 'fecha_hora_inicio',
                   'fecha_hora_finalizacion', 'cap')
    list_per_page = 10


class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero',)
    search_fields = ('id', 'numero',)
    list_filter = ('id', 'numero',)
    list_per_page = 10


class TipoDeDocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion',)
    search_fields = ('id', 'nombre', 'descripcion',)
    list_filter = ('id', 'nombre', 'descripcion',)
    list_per_page = 10


class UnidadDeMedidaAdmin(admin.ModelAdmin):
    list_display = ('id', 'unidad', 'descripcion',)
    search_fields = ('id', 'unidad', 'descripcion',)
    list_filter = ('id', 'unidad', 'descripcion',)
    list_per_page = 10


# Registering models

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Domicilio, DomicilioAdmin)
admin.site.register(EstadoDeSolicitud, EstadoDeSolicitudAdmin)
admin.site.register(Estudio, EstudioAdmin)
admin.site.register(Extraccionista, ExtraccionistaAdmin)
admin.site.register(Metodo, MetodoAdmin)
admin.site.register(Muestra, MuestraAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Resultado, ResultadoAdmin)
admin.site.register(Sexo, SexoAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Telefono, TelefonoAdmin)
admin.site.register(TipoDeDocumento, TipoDeDocumentoAdmin)
admin.site.register(UnidadDeMedida, UnidadDeMedidaAdmin)
