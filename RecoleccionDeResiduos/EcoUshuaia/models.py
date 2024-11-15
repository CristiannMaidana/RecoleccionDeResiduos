# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Calendarios(models.Model):
    id_calendario = models.AutoField(primary_key=True)
    novedad_calendario = models.CharField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)


class Contenedores(models.Model):
    id_contenedor = models.AutoField(primary_key=True)
    nombre_contenedor = models.CharField(max_length=30)
    id_zona = models.ForeignKey('Zonas', models.DO_NOTHING, db_column='id_zona')
    id_residuo = models.ForeignKey('Residuos', models.DO_NOTHING, db_column='id_residuo')
    id_coordenada = models.ForeignKey('Coordenadas', models.DO_NOTHING, db_column='id_coordenada')


class Coordenadas(models.Model):
    id_coordenada = models.AutoField(primary_key=True)
    coordenada = models.TextField(blank=True, null=True)  # This field type is a guess.


class Estados(models.Model):
    id_estado = models.AutoField(primary_key=True)
    estado_actual = models.IntegerField(blank=True, null=True)
    fecha = models.DateField(blank=True, null=True)
    hora = models.TimeField(blank=True, null=True)
    id_sensor = models.ForeignKey('Sensores', models.DO_NOTHING, db_column='id_sensor')


class Mapas(models.Model):
    id_mapa = models.AutoField(primary_key=True)
    nombre_mapa = models.CharField(max_length=30)


class Residuos(models.Model):
    id_residuo = models.AutoField(primary_key=True)
    nombre_residuos = models.CharField(max_length=30)


class Sensores(models.Model):
    id_sensor = models.AutoField(primary_key=True)
    nombre_sensor = models.CharField(max_length=30)
    id_contenedor = models.ForeignKey(Contenedores, models.DO_NOTHING, db_column='id_contenedor')


class Usuarios(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=35)
    apellido = models.CharField(max_length=35)
    usuario = models.CharField(max_length=35)
    dni = models.IntegerField(unique=True)
    email = models.CharField(unique=True, max_length=40)
    id_zona = models.ForeignKey('Zonas', models.DO_NOTHING, db_column='id_zona', blank=True, null=True)


class Zonas(models.Model):
    id_zona = models.AutoField(primary_key=True)
    nombre_zonas = models.CharField(max_length=10)
    color_zonas = models.CharField(max_length=10)
    id_mapa = models.ForeignKey(Mapas, models.DO_NOTHING, db_column='id_mapa')
    id_calendario = models.ForeignKey(Calendarios, models.DO_NOTHING, db_column='id_calendario', blank=True, null=True)
    id_coordenada = models.ForeignKey(Coordenadas, models.DO_NOTHING, db_column='id_coordenada')
