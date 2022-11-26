# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Domicilio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    calle = models.CharField(db_column='CALLE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    altura = models.IntegerField(db_column='ALTURA', blank=True, null=True)  # Field name made lowercase.
    n_piso = models.IntegerField(db_column='N_PISO', blank=True, null=True)  # Field name made lowercase.
    departamento = models.CharField(db_column='DEPARTAMENTO', max_length=15, blank=True,
                                    null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.calle} {self.altura} {self.n_piso} {self.departamento}"

    class Meta:
        managed = False
        db_table = 'DOMICILIO'


class EstadoDeSolicitud(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    descripccion = models.TextField(db_column='DESCRIPCCION', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'ESTADO_DE_SOLICITUD'


class Estudio(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descripccion = models.TextField(db_column='DESCRIPCCION', blank=True, null=True)  # Field name made lowercase.
    limite_inferior = models.FloatField(db_column='LIMITE_INFERIOR', blank=True,
                                        null=True)  # Field name made lowercase.
    limite_superior = models.FloatField(db_column='LIMITE_SUPERIOR', blank=True,
                                        null=True)  # Field name made lowercase.
    id_metodo = models.ForeignKey('Metodo', on_delete=models.CASCADE, db_column='ID_METODO', blank=True,
                                  null=True)  # Field name made lowercase.
    id_unidad_de_medida = models.ForeignKey('UnidadDeMedida', on_delete=models.CASCADE, db_column='ID_UNIDAD_DE_MEDIDA',
                                            blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'ESTUDIO'


class Extraccionista(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        managed = False
        db_table = 'EXTRACCIONISTA'


class Medico(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    matricula = models.CharField(db_column='MATRICULA', max_length=13, blank=True,
                                 null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        managed = False
        db_table = 'MEDICO'


class Metodo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    descripccion = models.TextField(db_column='DESCRIPCCION', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'METODO'


class Muestra(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    descripccion = models.TextField(db_column='DESCRIPCCION', blank=True, null=True)  # Field name made lowercase.
    fecha_hora_extraccion = models.DateTimeField(db_column='FECHA_HORA_EXTRACCION', blank=True,
                                                 null=True)  # Field name made lowercase.
    id_resultado = models.ForeignKey('Resultado', on_delete=models.CASCADE, db_column='ID_RESULTADO', blank=True,
                                     null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MUESTRA'


class Paciente(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    n_documento = models.IntegerField(db_column='N_DOCUMENTO', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    apellido = models.CharField(db_column='APELLIDO', max_length=50, blank=True,
                                null=True)  # Field name made lowercase.
    id_sexo = models.ForeignKey('Sexo', on_delete=models.CASCADE, db_column='ID_SEXO', blank=True,
                                null=True)  # Field name made lowercase.
    id_domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE, db_column='ID_DOMICILIO', blank=True,
                                     null=True)  # Field name made lowercase.
    id_telefono = models.ForeignKey('Telefono', on_delete=models.CASCADE, db_column='ID_TELEFONO', blank=True,
                                    null=True)  # Field name made lowercase.
    id_tipo_de_documento = models.ForeignKey('TipoDeDocumento', on_delete=models.CASCADE,
                                             db_column='ID_TIPO_DE_DOCUMENTO',
                                             blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        managed = False
        db_table = 'PACIENTE'


class Sexo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    descripccion = models.TextField(db_column='DESCRIPCCION', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'SEXO'


class Solicitud(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    receta = models.CharField(db_column='RECETA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, db_column='ID_PACIENTE', blank=True,
                                    null=True)  # Field name made lowercase.
    id_extraccionista = models.ForeignKey(Extraccionista, on_delete=models.CASCADE, db_column='ID_EXTRACCIONISTA',
                                          blank=True,
                                          null=True)  # Field name made lowercase.
    id_estado = models.ForeignKey(EstadoDeSolicitud, on_delete=models.CASCADE, db_column='ID_ESTADO', blank=True,
                                  null=True)  # Field name made lowercase.
    id_medico = models.ForeignKey(Medico, on_delete=models.CASCADE, db_column='ID_MEDICO', blank=True,
                                  null=True)  # Field name made lowercase.
    fecha_hora_inicio = models.DateTimeField(db_column='FECHA_HORA_INICIO', blank=True,
                                             null=True)  # Field name made lowercase.
    fecha_hora_finalizacion = models.DateTimeField(db_column='FECHA_HORA_FINALIZACION', blank=True,
                                                   null=True)  # Field name made lowercase.
    cap = models.CharField(db_column='CAP', max_length=8, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SOLICITUD'


class Resultado(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    valor_hallado = models.FloatField(db_column='VALOR_HALLADO', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField(db_column='FECHA', blank=True, null=True)  # Field name made lowercase.
    id_estudio = models.ForeignKey(Estudio, on_delete=models.CASCADE, db_column='ID_ESTUDIO', blank=True,
                                   null=True)  # Field name made lowercase.
    id_solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, db_column='ID_SOLICITUD', blank=True,
                                     null=True)
    observacion = models.TextField(db_column='OBSERVACION', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.valor_hallado}"

    class Meta:
        managed = False
        db_table = 'RESULTADO'


class Telefono(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero = models.BigIntegerField(db_column='NUMERO', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f"{self.numero}"

    class Meta:
        managed = False
        db_table = 'TELEFONO'


class TipoDeDocumento(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='NOMBRE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.nombre

    class Meta:
        managed = False
        db_table = 'TIPO_DE_DOCUMENTO'


class UnidadDeMedida(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='UNIDAD', max_length=15, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.TextField(db_column='DESCRIPCION', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.unidad

    class Meta:
        managed = False
        db_table = 'UNIDAD_DE_MEDIDA'
