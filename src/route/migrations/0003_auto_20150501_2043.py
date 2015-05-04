# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0002_auto_20150428_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of journey'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='arrival',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Arrival Time'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='departure',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Departure Time'),
        ),
    ]
