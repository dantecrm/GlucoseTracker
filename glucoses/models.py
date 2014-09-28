# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from core.models import TimeStampedModel
from django.core.validators import MinValueValidator, MaxValueValidator
from taggit.managers import TaggableManager

class Glucose(TimeStampedModel):
    # objects = GlucoseManager()

    user = models.ForeignKey(User)
    value = models.PositiveIntegerField(validators=[MaxValueValidator(54054),
                                                    MinValueValidator(0)])
    category = models.ForeignKey('Category')
    record_date = models.DateField('Date')
    record_time = models.TimeField('Time')
    notes = models.TextField('Notes', null=False, blank=True, default='')
    tags = TaggableManager(blank=True, help_text=None)

    def __unicode__(self):
        return str(self.value)

    class Meta:
        ordering = ['-record_date', '-record_time']


class Category(models.Model):

    """
    Modelo que contiene los alimentos durante el día, hora de dormir.
    """
    name = models.CharField(unique=True, max_length=255)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class Unit(models.Model):
    """
    Modelo que registra las unidades de medida de la glucosa: mmol/L, mg/dL.
    """
    name = models.CharField(unique=True, max_length=9)

    def __unicode__(self):
        return self.name
