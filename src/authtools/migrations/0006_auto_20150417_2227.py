# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('authtools', '0005_auto_20150416_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='dob',
            field=models.DateField(default=datetime.date(2015, 4, 17), verbose_name='date of birth'),
        ),
    ]
