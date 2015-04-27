# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 20, 28, 1, 990466), verbose_name='Date of journey'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='arrival',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 20, 28, 1, 989891), verbose_name='Arrival Time'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='departure',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 20, 28, 1, 989943), verbose_name='Departure Time'),
        ),
    ]
