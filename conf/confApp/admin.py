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

# Registering models

admin.site.register(Medico)
admin.site.register(Domicilio)
admin.site.register(EstadoDeSolicitud)
admin.site.register(Estudio)
admin.site.register(Extraccionista)
admin.site.register(Metodo)
admin.site.register(Muestra)
admin.site.register(Paciente)
admin.site.register(Resultado)
admin.site.register(Sexo)
admin.site.register(Solicitud)
admin.site.register(Telefono)
admin.site.register(TipoDeDocumento)
admin.site.register(UnidadDeMedida)
