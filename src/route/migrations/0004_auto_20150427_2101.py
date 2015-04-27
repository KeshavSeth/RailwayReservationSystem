# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0003_auto_20150427_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='schedule',
        ),
        migrations.AlterField(
            model_name='route',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 21, 1, 7, 178173), verbose_name='Date of journey'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='arrival',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 21, 1, 7, 176715), verbose_name='Arrival Time'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='departure',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 21, 1, 7, 176839), verbose_name='Departure Time'),
        ),
    ]
