# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gactividades', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividades',
            options={'permissions': (('listar_app_actividades', 'Puede ver la lista de la app actividades'), ('agregar_app_actividades', 'Puede agregar la lista de la app actividades'), ('modificar_app_actividades', 'Puede modificar la lista de la app actividades'), ('eliminar_app_actividades', 'Puede eliminar la lista de la app actividades'))},
        ),
    ]
