# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0004_auto_20150427_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 21, 2, 25, 469219), verbose_name='Date of journey'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='arrival',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 21, 2, 25, 468619), verbose_name='Arrival Time'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='departure',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 21, 2, 25, 468671), verbose_name='Departure Time'),
        ),
    ]
