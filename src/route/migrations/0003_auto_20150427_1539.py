# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0002_auto_20150427_1001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='date',
        ),
        migrations.AddField(
            model_name='route',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 27, 15, 39, 6, 270343), verbose_name='Date of journey'),
        ),
    ]
