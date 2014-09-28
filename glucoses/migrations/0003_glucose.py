# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('glucoses', '0002_auto_20140928_1752'),
    ]

    operations = [
        migrations.CreateModel(
            name='Glucose',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('value', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(54054), django.core.validators.MinValueValidator(0)])),
                ('record_date', models.DateField(verbose_name=b'Date')),
                ('record_time', models.TimeField(verbose_name=b'Time')),
                ('notes', models.TextField(default=b'', verbose_name=b'Notes', blank=True)),
                ('category', models.ForeignKey(to='glucoses.Category')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text=None, verbose_name='Tags')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-record_date', '-record_time'],
            },
            bases=(models.Model,),
        ),
    ]
