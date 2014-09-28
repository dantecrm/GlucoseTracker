#! coding: utf-8
from django.db import models

class TimeStampedModel(models.Model):
    """
    Clase base abstracta que provee auto-actualización 'crea' y 'midifica'
    los campos.

    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
