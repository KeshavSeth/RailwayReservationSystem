# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0005_auto_20150427_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='schedule',
            field=models.ManyToManyField(related_name='stations', to='route.StationSchedule'),
        ),
        migrations.AlterField(
            model_name='route',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 21, 3, 4, 698284), verbose_name='Date of journey'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='arrival',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 21, 3, 4, 697699), verbose_name='Arrival Time'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='departure',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 21, 3, 4, 697752), verbose_name='Departure Time'),
        ),
    ]
