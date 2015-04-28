# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0006_auto_20150427_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 5, 1, 58, 957909), verbose_name='Date of journey'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='arrival',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 5, 1, 58, 957313), verbose_name='Arrival Time'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='departure',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 28, 5, 1, 58, 957367), verbose_name='Departure Time'),
        ),
        migrations.AlterField(
            model_name='stationschedule',
            name='station',
            field=models.ForeignKey(to='station.Station'),
        ),
        migrations.DeleteModel(
            name='Station',
        ),
    ]
