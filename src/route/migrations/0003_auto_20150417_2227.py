# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0002_auto_20150416_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 17), verbose_name='Date of journey'),
        ),
    ]
