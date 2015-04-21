# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('route', '0003_auto_20150417_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='date',
            field=models.DateField(default=datetime.date(2015, 4, 21), verbose_name='Date of journey'),
        ),
    ]
