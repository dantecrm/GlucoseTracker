# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gactividades', '0003_auto_20141030_1033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hacer',
            options={'permissions': (('listar_app_hacer', 'Puede ver la lista de la app gactividades'), ('agregar_app_hacer', 'Puede agregar la lista de la app gactividades'), ('modificar_app_hacer', 'Puede modificar la lista de la app gactividades'), ('eliminar_app_hacer', 'Puede eliminar la lista de la app gactividades'))},
        ),
    ]
