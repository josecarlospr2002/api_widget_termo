from django.db import models

class Bloque1(models.Model):
    presion = models.FloatField()
    temperatura = models.FloatField()
    calor = models.FloatField()
    potencia = models.FloatField()
    potencia_calor = models.FloatField()
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bloque_1'


class Bloque2(models.Model):
    presion = models.FloatField()
    temperatura = models.FloatField()
    calor = models.FloatField()
    potencia = models.FloatField()
    potencia_calor = models.FloatField()
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bloque_2'


class Bloque3(models.Model):
    presion = models.FloatField()
    temperatura = models.FloatField()
    calor = models.FloatField()
    potencia = models.FloatField()
    potencia_calor = models.FloatField()
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bloque_3'