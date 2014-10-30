# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gactividades', '0002_auto_20141030_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hacer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('prioridad', models.PositiveSmallIntegerField(default=5, choices=[(0, b'Bajo'), (5, b'Normal'), (10, b'Alta'), (15, b'Urgente')])),
                ('agregado_en', models.DateTimeField(auto_now_add=True)),
                ('fecha_limite', models.DateField()),
                ('duenio', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('listar_app_hacer', 'Puede ver la lista de la app hacer'), ('agregar_app_hacer', 'Puede agregar la lista de la app hacer'), ('modificar_app_hacer', 'Puede modificar la lista de la app hacer'), ('eliminar_app_hacer', 'Puede eliminar la lista de la app hacer')),
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='actividades',
            name='duenio',
        ),
        migrations.DeleteModel(
            name='actividades',
        ),
    ]
