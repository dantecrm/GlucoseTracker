# coding: utf-8
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings
from timezone_field import TimeZoneField

from core.models import TimeStampedModel
from glucoses.models import Category, Unit


class Account(models.Model):
	user = models.OneToOneField(User)
	birthday = models.DateField()
	name = models.CharField(max_length=100)

	def __unicode__(self):
		return self.name

	def create_user_profile(sender, instance, created, **kwargs):
		if created :
			Account.objects.create(user=instance)
		post_save.connect(create_user_profile, sender=User)

class UserSettings(TimeStampedModel):
    """
    Modelo para almacenar la configuración y preferencias de usuarios
    adicionales.
    Extiende el modelo user.
    """

    user = models.OneToOneField(User, related_name='settings')
    time_zone = TimeZoneField(default=settings.TIME_ZONE)

    glucose_unit = models.ForeignKey(Unit, null=False, blank=False, default=1)
    default_category = models.ForeignKey(Category, null=True)

    glucose_low = models.PositiveIntegerField(null=False, blank=False, default=60)
    glucose_high = models.PositiveIntegerField(null=False, blank=False, default=180)
    glucose_target_min =  models.PositiveIntegerField(null=False, blank=False, default=70)
    glucose_target_max =  models.PositiveIntegerField(null=False, blank=False, default=120)

    def username(self):
        return self.user.username
    username.admin_order_field = 'user__username'

    class Meta:
        verbose_name_plural = 'Configuraciones de usuario'
