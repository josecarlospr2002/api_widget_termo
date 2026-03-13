from django.db import models

class Bloque1(models.Model):
    presion = models.FloatField()
    temperatura = models.FloatField()
    calor = models.FloatField()
    potencia = models.FloatField()
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bloque_1'
        verbose_name = "Bloque 1"
        verbose_name_plural = "Bloque 1"

    def __str__(self):
        return f"Bloque 1 - {self.fecha}"


class Bloque2(models.Model):
    presion = models.FloatField()
    temperatura = models.FloatField()
    calor = models.FloatField()
    potencia = models.FloatField()
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bloque_2'
        verbose_name = "Bloque 2"
        verbose_name_plural = "Bloque 2"

    def __str__(self):
        return f"Bloque 2 - {self.fecha}"


class Bloque3(models.Model):
    presion = models.FloatField()
    temperatura = models.FloatField()
    calor = models.FloatField()
    potencia = models.FloatField()
    fecha = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bloque_3'
        verbose_name = "Bloque 3"
        verbose_name_plural = "Bloque 3"

    def __str__(self):
        return f"Bloque 3 - {self.fecha}"