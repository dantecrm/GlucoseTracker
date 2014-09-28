# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20140928_1649'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usersettings',
            options={'verbose_name_plural': 'Configuraciones de usuario'},
        ),
        migrations.RenameField(
            model_name='usersettings',
            old_name='glucose_category',
            new_name='default_category',
        ),
    ]
