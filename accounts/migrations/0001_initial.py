# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                (b'time_zone', timezone_field.fields.TimeZoneField(max_length=63)),
                ('glucose_low', models.PositiveIntegerField(default=60)),
                ('glucose_high', models.PositiveIntegerField(default=180)),
                ('glucose_target_min', models.PositiveIntegerField(default=70)),
                ('glucose_target_max', models.PositiveIntegerField(default=120)),
                ('user', models.OneToOneField(related_name=b'settings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
