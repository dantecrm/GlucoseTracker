# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# - titulo: maximo 50
# - descrpción: sin maximo
# - dueño: extiende de User
# - fecha y hora de creación: agregado_en: fecha y hora
# - fecha límite: fecha_limite: DateField
# - prioridad(elegible: lista_prioridad, por defecto debe ser normal)

class Hacer(models.Model):
    LISTA_PRIORIDADES = (
        (0,'Bajo'),
        (5,'Normal'),
        (10,'Alta'),
        (15,'Urgente'),
    )

    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    duenio = models.OneToOneField(User)
    prioridad = models.PositiveSmallIntegerField(choices=LISTA_PRIORIDADES, default=5)
    agregado_en = models.DateTimeField(auto_now_add = True)
    fecha_limite = models.DateField()

    class Meta:
        permissions = (
            ('listar_app_hacer', 'Puede ver la lista de la app gactividades'),
            ('agregar_app_hacer', 'Puede agregar la lista de la app gactividades'),
            ('modificar_app_hacer', 'Puede modificar la lista de la app gactividades'),
            ('eliminar_app_hacer', 'Puede eliminar la lista de la app gactividades'),
        )

    def __unicode__(self):
        return u"%s" % self.titulo
