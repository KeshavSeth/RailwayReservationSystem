# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0003_auto_20150427_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 15, 41, 59, 323774), verbose_name='Date of journey'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='arrival',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 15, 41, 59, 323213), verbose_name='Arrival Time'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='departure',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 15, 41, 59, 323263), verbose_name='Departure Time'),
        ),
    ]
