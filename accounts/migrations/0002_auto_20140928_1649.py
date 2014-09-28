# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glucoses', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='glucose_category',
            field=models.ForeignKey(to='glucoses.Category', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='usersettings',
            name='glucose_unit',
            field=models.ForeignKey(default=1, to='glucoses.Unit'),
            preserve_default=True,
        ),
    ]
